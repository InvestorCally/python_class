def file():
    import random
    import group1 as gp
    Account_name, Password = gp.reg()
    Account_num = random.randint(100000000, 999999999)
    Account_bal = random.randint(0,100000)

    account_file = {
    'account_details': Account_name,
    'account_password': Password,
    'account_balance': Account_bal,
    'account_number': Account_num
    }
    return account_file

     