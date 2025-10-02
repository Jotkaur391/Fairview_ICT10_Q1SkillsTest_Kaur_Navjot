from pyscript import document, display

# Menu and prices
menu_prices = {
    "Chestnut Ice Cream": 100,
    "Makgeolli Ice Cream": 120,
    "Corn Ice Cream": 90,
    "Green Tea Ice Cream": 110,
    "Sweet Potato Ice Cream": 130
}

def compute_order(event):
    # Get customer info
    name = document.getElementById("cust_name").value or "Unknown"
    address = document.getElementById("cust_address").value or "N/A"
    contact = document.getElementById("cust_contact").value or "N/A"

    # Determine selected items
    selected_items = []
    total = 0

    if document.getElementById("item1").checked:
        selected_items.append("Chestnut Ice Cream")
        total += menu_prices["Chestnut Ice Cream"]
    if document.getElementById("item2").checked:
        selected_items.append("Makgeolli Ice Cream")
        total += menu_prices["Makgeolli Ice Cream"]
    if document.getElementById("item3").checked:
        selected_items.append("Corn Ice Cream")
        total += menu_prices["Corn Ice Cream"]
    if document.getElementById("item4").checked:
        selected_items.append("Green Tea Ice Cream")
        total += menu_prices["Green Tea Ice Cream"]
    if document.getElementById("item5").checked:
        selected_items.append("Sweet Potato Ice Cream")
        total += menu_prices["Sweet Potato Ice Cream"]

    # Build order summary
    if selected_items:
        items_str = "\n".join(f"🍦 {item} - ₱{menu_prices[item]}" for item in selected_items)
    else:
        items_str = "No items selected."

    summary_text = f"""📝 Order Summary:
👤 Customer Name: {name}
🏠 Address: {address}
📞 Contact: {contact}

🍨 Ordered Items:
{items_str}

💰 Total Amount: ₱{total}
"""

    document.getElementById("summary").innerText = summary_text
