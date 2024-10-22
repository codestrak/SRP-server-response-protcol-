import requests
import webbrowser

def get_auth_token():
    # Prompt user for auth token
    auth_token = input("Enter your auth token: ")
    return auth_token

def store_auth_token(auth_token):
    # Store the auth token securely (for demonstration, we will just print it)
    # In a real application, consider using a secure storage method
    print(f"Storing auth token: {auth_token}")
    return auth_token

def redirect_to_admin_console(auth_token):
    # Redirect to admin console using the stored auth token
    admin_console_url = "https://admin-console.example.com"
    headers = {
        'Authorization': f'Bearer {auth_token}'
    }
    
    # Simulate a request to the admin console
    response = requests.get(admin_console_url, headers=headers)
    
    if response.status_code == 200:
        print("You are now logged in to the admin console.")
    else:
        print("Failed to log in to the admin console. Please check your auth token.")

def main():
    auth_token = get_auth_token()
    stored_token = store_auth_token(auth_token)
    redirect_to_admin_console(stored_token)

if __name__ == "__main__":
    main()
