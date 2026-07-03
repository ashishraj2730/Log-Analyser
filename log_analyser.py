from collections import Counter
from datetime import datetime

print("=" * 60)
print("            LOG ANALYZER")
print("=" * 60)

log_file = input("Enter Log File Name: ").strip()

failed_logins = 0
successful_logins = 0
ip_counter = Counter()

try:
    with open(log_file, "r") as file:
        lines = file.readlines()

    total_logs = len(lines)

    for line in lines:

        if "Failed password" in line:
            failed_logins += 1

            if "from" in line:
                ip = line.split("from")[-1].strip()
                ip_counter[ip] += 1

        elif "Accepted password" in line:
            successful_logins += 1

    print("\n" + "=" * 60)
    print("LOG ANALYSIS REPORT")
    print("=" * 60)

    print(f"Total Log Entries      : {total_logs}")
    print(f"Failed Login Attempts  : {failed_logins}")
    print(f"Successful Logins      : {successful_logins}")

    print("\nSuspicious IP Addresses")
    print("-" * 60)

    suspicious_found = False

    for ip, count in ip_counter.items():
        if count >= 2:
            print(f"{ip}  --> {count} Failed Attempts")
            suspicious_found = True

    if not suspicious_found:
        print("No Suspicious IP Found")

    report_name = f"log_report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"

    with open(report_name, "w") as report:

        report.write("LOG ANALYSIS REPORT\n")
        report.write("=" * 50 + "\n")
        report.write(f"Date : {datetime.now()}\n\n")

        report.write(f"Total Log Entries : {total_logs}\n")
        report.write(f"Failed Logins : {failed_logins}\n")
        report.write(f"Successful Logins : {successful_logins}\n\n")

        report.write("Suspicious IP Addresses\n")
        report.write("-" * 40 + "\n")

        if suspicious_found:
            for ip, count in ip_counter.items():
                if count >= 2:
                    report.write(f"{ip} --> {count} Failed Attempts\n")
        else:
            report.write("No Suspicious IP Found\n")

    print("\nReport Saved :", report_name)

except FileNotFoundError:
    print("\nError: Log file not found.")
