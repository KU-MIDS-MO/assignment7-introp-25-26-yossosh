def make_account(initial_balance):
    ### Replace with your own code (begin) ###
    if not isinstance(initial_balance, (int, float)):
        raise TypeError("initial balance must be a number")
    
    if initial_balance < 0:
        raise ValueError("initial balance must be non-negative")
        
    balance = initial_balance
        
        
    def deposit(amount):
        nonlocal balance
        
        if not isinstance(amount, (int, float)):
            raise TypeError("amount must be a number")
        
        if amount <= 0:
            raise ValueError("amount must be positive")
            
        balance += amount
        
        return balance
        
        
    def withdraw(amount):
        nonlocal balance
        
        if not isinstance(amount, (int, float)):
            raise TypeError("amount must be a number")
        
        if amount <= 0:
            raise ValueError("amount must be positive")
            
        if amount <= balance:
            balance -= amount
        else:
            raise ValueError("amount is too big")
        
        return balance
    
    
    return deposit, withdraw
    ### Replace with your own code (end)   ###
