def email_slicer():
    """Slices an email address into its username and domain."""
    print("Welcome to the Email Slicer!")
    print("Enter an email address to get the username and domain.")
    
    email_address = input("Enter email address: ").strip()

    try:
        # Find the index of the '@' symbol
        at_index = email_address.index('@')
        
        # Slice the string to get the username and domain
        username = email_address[:at_index]
        domain = email_address[at_index + 1:]
        
        print(f"\nUsername: {username}")
        print(f"Domain: {domain}")
        
    except ValueError:
        print("\nInvalid email address. Please make sure it contains an '@' symbol.")

# Run the function
email_slicer()
