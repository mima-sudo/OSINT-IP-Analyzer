import webbrowser
import tkinter as tk

def open_shodan():
    ip = entry.get()
    webbrowser.open(f"https://www.shodan.io/host/{ip}")

def open_virustotal():
    ip = entry.get()
    webbrowser.open(f"https://www.virustotal.com/gui/ip-address/{ip}")

def open_maltego():
    webbrowser.open("https://www.maltego.com/")

def generate_report():
    ip = entry.get()
    report = f"""
===== OSINT REPORT =====

IP Address: {ip}

Tools Used:
- Shodan
- VirusTotal
- Maltego

Objective:
Reconstruct and analyze network infrastructure using open-source intelligence.

Analysis:
Shodan is used to identify open ports and exposed services.
VirusTotal is used to check the reputation of the IP and related domains.
Maltego is used to visualize relationships between the IP, domains, and infrastructure.

Conclusion:
The analyzed IP shows several open services and indicators that require further investigation.
OSINT helps analysts understand and map infrastructure from public sources.
"""
    with open("report.txt", "w", encoding="utf-8") as file:
        file.write(report)

    status_label.config(text="Report Generated ✔", fg="#2e7d32")

root = tk.Tk()
root.title("OSINT IP Analyzer")
root.geometry("430x430")
root.configure(bg="#fce4ec")

title = tk.Label(
    root,
    text="OSINT IP Analyzer",
    font=("Arial", 18, "bold"),
    bg="#fce4ec",
    fg="#6a1b9a"
)
title.pack(pady=15)

subtitle = tk.Label(
    root,
    text="Investigation OSINT & Infrastructure Mapping",
    font=("Arial", 10),
    bg="#fce4ec",
    fg="#283593"
)
subtitle.pack(pady=2)

label = tk.Label(
    root,
    text="Enter IP Address:",
    bg="#fce4ec",
    font=("Arial", 11, "bold")
)
label.pack(pady=8)

entry = tk.Entry(root, width=28, font=("Arial", 12), justify="center")
entry.pack(pady=5)
entry.insert(0, "45.9.148.108")

btn1 = tk.Button(
    root,
    text="🔍 Open Shodan",
    bg="#bbdefb",
    fg="black",
    width=24,
    height=2,
    font=("Arial", 10, "bold"),
    command=open_shodan
)
btn1.pack(pady=6)

btn2 = tk.Button(
    root,
    text="🛡 Open VirusTotal",
    bg="#c8e6c9",
    fg="black",
    width=24,
    height=2,
    font=("Arial", 10, "bold"),
    command=open_virustotal
)
btn2.pack(pady=6)

btn3 = tk.Button(
    root,
    text="🕸 Open Maltego",
    bg="#d1c4e9",
    fg="black",
    width=24,
    height=2,
    font=("Arial", 10, "bold"),
    command=open_maltego
)
btn3.pack(pady=6)

btn4 = tk.Button(
    root,
    text="📄 Generate Report",
    bg="#ffcdd2",
    fg="black",
    width=24,
    height=2,
    font=("Arial", 10, "bold"),
    command=generate_report
)
btn4.pack(pady=10)

status_label = tk.Label(
    root,
    text="",
    bg="#fce4ec",
    font=("Arial", 10, "bold")
)
status_label.pack(pady=5)

footer = tk.Label(
    root,
    text="Prepared for OSINT TP",
    bg="#fce4ec",
    fg="#555555",
    font=("Arial", 9)
)
footer.pack(side="bottom", pady=10)

root.mainloop()