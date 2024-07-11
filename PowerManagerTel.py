import subprocess
import re

def get_cpu_power():
    result = subprocess.run(['sudo', 'powertop', '--html=powertop.html'], capture_output=True, text=True)
   
    with open('powertop.html', 'r') as file:
        data = file.read()
    match = re.search(r'Processor\s+\d+\s+:\s+(\d+\.\d+)\s+W', data)
    cpu_power = float(match.group(1)) if match else 0.0
    return cpu_power

def get_gpu_power():
    result = subprocess.run(['nvidia-smi', '--query-gpu=power.draw', '--format=csv,noheader,nounits'], capture_output=True, text=True)
    power_draw = float(result.stdout.strip())  
    return power_draw

def get_nic_power(interface):
    result = subprocess.run(['sudo', 'ethtool', interface], capture_output=True, text=True)
    output = result.stdout
  
    match = re.search(r'Current message level\s+:\s+(\d+)', output)
    nic_power = float(match.group(1)) if match else 0.0
    return nic_power

def calculate_power_consumption(battery_percentage, battery_capacity_wh):
    remaining_capacity_wh = battery_capacity_wh * (battery_percentage / 100.0)
    
    cpu_power = get_cpu_power()
    gpu_power = get_gpu_power()
    nic_power = get_nic_power('eth0')  
    
    total_power = cpu_power + gpu_power + nic_power
    power_ratios = {
        'CPU': cpu_power / total_power if total_power > 0 else 0.0,
        'GPU': gpu_power / total_power if total_power > 0 else 0.0,
        'NIC': nic_power / total_power if total_power > 0 else 0.0
    }
    
    power_consumption = {
        'CPU': remaining_capacity_wh * power_ratios['CPU'],
        'GPU': remaining_capacity_wh * power_ratios['GPU'],
        'NIC': remaining_capacity_wh * power_ratios['NIC']
    }
    
    return power_consumption

if _name_ == "_main_":
    battery_percentage = float(input("Enter battery percentage: "))
    battery_capacity_wh = 50 
    power_consumption = calculate_power_consumption(battery_percentage, battery_capacity_wh)
    print(f"Power Consumption (Wh): {power_consumption}")