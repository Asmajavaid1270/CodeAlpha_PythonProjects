import json
from datetime import datetime
from typing import Dict, List
from pathlib import Path

class PortfolioManager:
    def __init__(self):
        self.STOCK_PRICES: Dict[str, float] = {
            "apple": 150.00, "tesla": 200.50, "google": 180.25, "amazon": 170.75
        }
        self.portfolio: List[Dict] = []
        self.data_file: Path = Path("data/portfolio.json")

    def _ensure_data_dir(self):
        self.data_file.parent.mkdir(exist_ok=True)

    def add_stock(self, name: str, quantity: int) -> bool:
        if name not in self.STOCK_PRICES:
            return False
        price = self.STOCK_PRICES[name]
        total = price * quantity
        self.portfolio.append({
            "stock": name.upper(), "quantity": quantity,
            "price": price, "total": total,
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        })
        return True

    def save_report(self):
        self._ensure_data_dir()
        grand_total = sum(item['total'] for item in self.portfolio)
        report = {
            "generated_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "items": self.portfolio, "grand_total": grand_total
        }
        with open(self.data_file, "w") as f:
            json.dump(report, f, indent=4)
        return grand_total

    def run(self):
        print("\n📈 === STOCK PORTFOLIO TRACKER === 📈")
        while True:
            name = input("Enter stock name (or 'done'): ").lower().strip()
            if name == "done":
                break
            if name not in self.STOCK_PRICES:
                print("❌ Stock not found in database.")
                continue
            try:
                qty = int(input("Enter quantity: "))
                if qty <= 0: raise ValueError
            except ValueError:
                print("⚠️ Please enter a valid positive number.")
                continue
            if self.add_stock(name, qty):
                print(f"✅ Added {qty} shares of {name.upper()}")
        if self.portfolio:
            total = self.save_report()
            print(f"\n💾 Report saved to {self.data_file}")
            print(f"💰 Total Investment: ${total:.2f}")
        else:
            print("\n⚠️ No stocks added.")

if __name__ == "__main__":
    manager = PortfolioManager()
    manager.run()