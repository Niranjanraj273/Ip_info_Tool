import requests
from colorama import Fore, Style, init
from prettytable import PrettyTable
import json
from datetime import datetime

# Initialize colorama
init(autoreset=True)

def fetch_ip_info(ip):
    """Fetch IP information from ipinfo.io API"""
    try:
        response = requests.get(f"https://ipinfo.io/{ip}/json")
        data = response.json()
        if "error" in data:
            print(Fore.RED + f"🚨 Error: {data['error']['message']}")
            return None
        return data
    except Exception as e:
        print(Fore.RED + f"🚨 Connection Error: {e}")
        return None

def display_ip_info(data):
    """Display IP information in a stylish format"""
    if not data:
        return

    # Create pretty table
    table = PrettyTable()
    table.field_names = [Fore.CYAN + "Category", Fore.CYAN + "Information"]
    table.align = "l"
    table.header_style = "upper"
    table.border = True
    table.horizontal_char = "═"
    table.vertical_char = "║"
    table.junction_char = "╬"

    # Add data to table with colors and emojis
    table.add_row([f"🌐 {Fore.YELLOW}IP Address", f"{Fore.WHITE}{data.get('ip', 'N/A')}"])
    table.add_row([f"🏷️ {Fore.YELLOW}Hostname", f"{Fore.WHITE}{data.get('hostname', 'N/A')}"])
    table.add_row([f"🏙️ {Fore.YELLOW}City", f"{Fore.GREEN}{data.get('city', 'N/A')}"])
    table.add_row([f"🗺️ {Fore.YELLOW}Region", f"{Fore.GREEN}{data.get('region', 'N/A')}"])
    table.add_row([f"🌍 {Fore.YELLOW}Country", f"{Fore.BLUE}{data.get('country', 'N/A')}"])
    table.add_row([f"📍 {Fore.YELLOW}Location", f"{Fore.MAGENTA}{data.get('loc', 'N/A')}"])
    table.add_row([f"🏢 {Fore.YELLOW}ISP", f"{Fore.CYAN}{data.get('org', 'N/A')}"])
    table.add_row([f"📮 {Fore.YELLOW}Postal Code", f"{Fore.WHITE}{data.get('postal', 'N/A')}"])
    table.add_row([f"⏰ {Fore.YELLOW}Timezone", f"{Fore.WHITE}{data.get('timezone', 'N/A')}"])

    # Display the table
    print(Fore.MAGENTA + "\n╔════════════════════════════════════╗")
    print(Fore.MAGENTA +  "║    🌟 IP INFORMATION REPORT 🌟     ║")
    print(Fore.MAGENTA +  "╚════════════════════════════════════╝")
    print(table)

    # Google Maps link
    if 'loc' in data:
        lat, lon = data['loc'].split(',')
        print(Fore.LIGHTGREEN_EX + f"\n🔗 Google Maps: {Style.BRIGHT}https://www.google.com/maps?q={lat},{lon}")

    # Export option
    export = input(Fore.YELLOW + "\n💾 Export to HTML? (y/n): " + Fore.WHITE).lower()
    if export == 'y':
        export_to_html(data)

def export_to_html(data):
    """Export IP info to HTML file"""
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    filename = f"ip_report_{timestamp}.html"
    
    html_content = f"""
    <html>
    <head>
        <title>IP Information Report</title>
        <style>
            body {{ font-family: Arial, sans-serif; margin: 20px; }}
            h1 {{ color: #4b2e83; }}
            table {{ border-collapse: collapse; width: 100%; margin-top: 20px; }}
            th {{ background-color: #4b2e83; color: white; padding: 10px; text-align: left; }}
            td {{ padding: 8px; border-bottom: 1px solid #ddd; }}
            .map-link {{ margin-top: 20px; }}
        </style>
    </head>
    <body>
        <h1>🌐 IP Information Report</h1>
        <p>Generated on: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}</p>
        
        <table>
            <tr><th>Category</th><th>Information</th></tr>
            <tr><td>IP Address</td><td>{data.get('ip', 'N/A')}</td></tr>
            <tr><td>Hostname</td><td>{data.get('hostname', 'N/A')}</td></tr>
            <tr><td>City</td><td>{data.get('city', 'N/A')}</td></tr>
            <tr><td>Region</td><td>{data.get('region', 'N/A')}</td></tr>
            <tr><td>Country</td><td>{data.get('country', 'N/A')}</td></tr>
            <tr><td>Location</td><td>{data.get('loc', 'N/A')}</td></tr>
            <tr><td>ISP</td><td>{data.get('org', 'N/A')}</td></tr>
            <tr><td>Postal Code</td><td>{data.get('postal', 'N/A')}</td></tr>
            <tr><td>Timezone</td><td>{data.get('timezone', 'N/A')}</td></tr>
        </table>
    """

    if 'loc' in data:
        lat, lon = data['loc'].split(',')
        html_content += f"""
        <div class="map-link">
            <p><a href="https://www.google.com/maps?q={lat},{lon}" target="_blank">📍 View on Google Maps</a></p>
        </div>
        """

    html_content += "</body></html>"

    with open(filename, 'w') as f:
        f.write(html_content)
    
    print(Fore.GREEN + f"\n✅ Report saved as {filename}")

def main():
    print(Fore.BLUE + Style.BRIGHT + """
    ███████╗██████╗ ██╗██████╗ ███████╗██████╗ 
    ██╔════╝██╔══██╗██║██╔══██╗██╔════╝██╔══██╗
    █████╗  ██████╔╝██║██████╔╝█████╗  ██████╔╝
    ██╔══╝  ██╔═══╝ ██║██╔═══╝ ██╔══╝  ██╔══██╗
    ███████╗██║     ██║██║     ███████╗██║  ██║
    ╚══════╝╚═╝     ╚═╝╚═╝     ╚══════╝╚═╝  ╚═╝
    """)
    
    print(Fore.CYAN + "🌟 Welcome to Advanced IP Info Tool 🌟")
    print(Fore.LIGHTBLUE_EX + "----------------------------------------")
    
    while True:
        ip = input(Fore.YELLOW + "\n🔍 Enter IP Address (or 'q' to quit): " + Fore.WHITE).strip()
        
        if ip.lower() == 'q':
            print(Fore.MAGENTA + "\n👋 Thank you for using the IP Info Tool!")
            break
            
        if not ip:
            ip = requests.get('https://api.ipify.org').text
            print(Fore.LIGHTBLUE_EX + f"\nℹ Using your public IP: {ip}")
            
        data = fetch_ip_info(ip)
        display_ip_info(data)
        
        choice = input(Fore.YELLOW + "\n🔁 Check another IP? (y/n): " + Fore.WHITE).lower()
        if choice != 'y':
            print(Fore.MAGENTA + "\n👋 Thank you for using the IP Info Tool!")
            break

if __name__ == "__main__":
    main()
