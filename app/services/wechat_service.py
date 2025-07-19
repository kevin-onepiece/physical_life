from printer import print_text, generate_payment_receipt, generate_todo_list, print_todo, print_bill

def handle_user_input(content, to_user, from_user):
    content = content.strip()
    if content.startswith("#记账"):
        bill_content = content[len("#记账"):].strip()
        items = []
        total = 0
        today_total = 0  # 可根据实际业务统计，这里先写死
        # 假设格式：买了牛奶 10元
        for part in bill_content.split(" "):
            if "元" in part:
                try:
                    total = int(part.replace("元", ""))
                except:
                    total = 0
        items.append((bill_content, total))
        receipt = generate_payment_receipt(total, items, today_total)
        print_text(receipt)
        return "已记录账单 ✅"
    elif content.startswith("#待办"):
        todo_content = content[len("#待办"):].strip()
        completed_count = 0  # 可根据实际业务统计，这里先写死
        todo = generate_todo_list(todo_content, completed_count)
        print_text(todo)
        return "待办事项已添加 📌"
    elif any(word in content for word in ["买了", "花了", "用了"]):
        bill_content = content
        items = []
        total = 0
        today_total = 0
        for part in bill_content.split(" "):
            if "元" in part:
                try:
                    total = int(part.replace("元", ""))
                except:
                    total = 0
        items.append((bill_content, total))
        receipt = generate_payment_receipt(total, items, today_total)
        print_text(receipt)
        return "已记录账单 ✅"
    else:
        completed_count = 0
        todo = generate_todo_list(content, completed_count)
        print_text(todo)
        return "待办事项已添加 📌"

def print_todo(content):
    # 这里用你的待办模板格式化
    todo_template = f"【待办清单】\n{content}\n----------------"
    print_text(todo_template)

def print_bill(content):
    # 这里用你的记账模板格式化
    bill_template = f"【记账】\n{content}\n----------------"
    print_text(bill_template)
