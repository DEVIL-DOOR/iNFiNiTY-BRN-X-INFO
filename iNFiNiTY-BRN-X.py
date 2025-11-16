import requests
import json
import os
import time

# ANSI Color Codes
class Colors:
    RED    = '\033[91m'
    GREEN  = '\033[92m'
    YELLOW = '\033[93m'
    BLUE   = '\033[94m'
    PURPLE = '\033[95m'
    CYAN   = '\033[96m'
    WHITE  = '\033[97m'
    BOLD   = '\033[1m'
    END    = '\033[0m'

# Custom Info
DEVELOPER = "Mr.Shuvo"
CHANNEL = "t.me/infinityerror2"
API_URL = "https://lmnx9.appletolha.com/BRN.info"

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def get_brn_info(brn):
    try:
        response = requests.get(API_URL, params={"brn": brn}, timeout=10)
        
        if response.status_code == 200:
            data = response.json()
            if data.get("is_success"):
                info = data["api_response"]
                print(f"\n{Colors.GREEN}BRN Information Retrieved Successfully!{Colors.END}\n")
                print(f"BRN Number     : {info['BRN_Number']}")
                print(f"Name (Bangla)  : {info['Name_Bn']}")
                print(f"Name (English) : {info['Name_En']}")
                print(f"Date of Birth  : {info['DOB']}")
                print(f"Birth Year     : {info['Year']}")
                print(f"Developer      : {Colors.BLUE}{DEVELOPER}{Colors.END}")
                print(f"Channel        : {Colors.BLUE}{CHANNEL}{Colors.END}")
            else:
                print(f"{Colors.RED}Failed to get valid response from API.{Colors.END}")
        else:
            print(f"{Colors.RED}HTTP Error: {response.status_code}{Colors.END}")
            print(response.text)
            
    except requests.exceptions.RequestException as e:
        print(f"{Colors.RED}Network Error: {e}{Colors.END}")
    except json.JSONDecodeError:
        print(f"{Colors.RED}Failed to decode JSON response.{Colors.END}")
    except Exception as e:
        print(f"{Colors.RED}Unknown Error: {e}{Colors.END}")

def main():
    clear_screen()
    
    # Colorful Header
    print(f"{Colors.RED}{'='*60}{Colors.END}")
    print(f"{Colors.RED}          NEW SESSION STARTED {Colors.END}")
    print(f"{Colors.GREEN}               iNFiNiTY ERROR BRN Tool{Colors.END}")
    print(f"{Colors.BLUE}                    Developer: {DEVELOPER}{Colors.END}")
    print(f"{Colors.BLUE}                    Channel: {CHANNEL}{Colors.END}")
    print(f"{Colors.YELLOW}               Time: {time.strftime('%Y-%m-%d %I:%M %p')}{Colors.END}")
    print(f"{Colors.RED}{'='*60}{Colors.END}")
    
    brn = input(f"\n{Colors.CYAN}Enter 17-digit BRN: {Colors.END}").strip()
    
    if not brn.isdigit() or len(brn) != 17:
        print(f"{Colors.RED}BRN must be exactly 17 digits and contain only numbers.{Colors.END}")
        input(f"\n{Colors.WHITE}Press Enter to exit...{Colors.END}")
        return
    
    get_brn_info(brn)
    
    print(f"\n{Colors.RED}{'='*60}{Colors.END}")
    print(f"{Colors.PURPLE}                Session Complete! Thank You!{Colors.END}")
    print(f"{Colors.CYAN}             Run again for a NEW SESSION{Colors.END}")
    print(f"{Colors.RED}{'='*60}{Colors.END}")
    input(f"\n{Colors.WHITE}Press Enter to close...{Colors.END}")

if __name__ == "__main__":
    main()