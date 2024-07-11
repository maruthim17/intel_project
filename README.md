

https://github.com/maruthim17/intel_project/assets/170094693/974fb513-4355-446b-80ff-b2a39f6a23a0

Power management telemetry using Windows Subsystem for Linux (WSL) leverages the integration of Linux tools within the Windows environment to monitor and optimize power usage. WSL allows users to run a Linux distribution directly on Windows, providing access to powerful command-line utilities and scripts without the overhead of a virtual machine. By utilizing tools such as powertop and upower, users can collect detailed telemetry data on power consumption, identify inefficient processes, and implement strategies to improve energy efficiency. This approach is particularly beneficial for developers and IT professionals who require a seamless workflow between Linux and Windows, enabling them to harness the strengths of both operating systems. The integration of WSL with power management telemetry not only simplifies the monitoring process but also enhances the accuracy and depth of the data collected, ultimately contributing to more informed decision-making and better resource management.
![image](https://github.com/maruthim17/intel_project/assets/170094693/dcb42055-e23e-480c-a536-c43eb514b47f)
![image](https://github.com/maruthim17/intel_project/assets/170094693/015f5b80-4e91-462b-b08a-f96cff118183)

1. Access to Advanced Linux Power Management Tools
powertop:
-Monitor power consumption by various system components.
-Identify power-hungry processes and optimize them.
-Generate detailed power consumption reports.
upower:
-Monitor battery status and power consumption of devices.
-Retrieve information about system power sources.
2. Low Overhead and Efficient Performance
Resource Efficiency:
-Minimal performance impact compared to virtual machines.
-Lightweight nature makes it suitable for continuous monitoring tasks.
ARCHITECTURE DIAGRAM![image](https://github.com/maruthim17/intel_project/assets/170094693/584f267b-90d8-4da9-8071-7a78cb9ab436)


![image](https://github.com/maruthim17/intel_project/assets/170094693/aff63f3c-efc9-486f-b655-398207c449ec)

TECHNOLOGIES USED:
Intel RAPL (Running Average Power Limit)
1.Purpose:
-RAPL provides mechanisms to monitor and control the power consumption of various components, including CPUs, DRAM, and potentially other components.
-It aims to optimize energy usage and enhance performance in power-sensitive applications.
2.Usage:
-Data Centers: Used to manage the power consumption of servers to reduce operational costs and improve energy efficiency.
-High-Performance Computing (HPC): Ensures that HPC systems operate within power limits to maintain performance while avoiding thermal issues.
-Power-Sensitive Applications: Essential in environments where power consumption needs to be strictly controlled, such as mobile devices and embedded systems.
Functionality:
Power Monitoring: Provides real-time data on the power consumption of various system components, allowing for detailed analysis.
Power Limiting: Enables setting of power limits for different components to prevent exceeding the thermal design power (TDP) and ensure safe operation.
Dynamic Adjustment: Allows for on-the-fly adjustments of power settings based on workload demands, optimizing performance and power efficiency.
Data Retrieval: Offers APIs to retrieve power consumption data, which can be used to make informed decisions about power management and system configuration.
![image](https://github.com/maruthim17/intel_project/assets/170094693/4c3dc83b-1b3e-48a8-99b5-08a816cf3378)
CONCLUSION

The Power Manager Telemetry Project using Intel's RAPL on Windows Subsystem for Linux (WSL) successfully demonstrated a system for monitoring, analyzing, and optimizing CPU and DRAM power consumption.
Key Achievements:
1.Data Collection:
-Developed Python scripts for continuous power data collection via Intel RAPL.
-Implemented a backend service for efficient data logging and storage.
2.Data Analysis:
-Identified power usage patterns and performance correlations.
In conclusion, the Power Manager Telemetry Project has laid a strong foundation for effective power monitoring and management using Intel RAPL and WSL. The insights gained and the tools developed will contribute significantly to enhancing energy efficiency and performance optimization in various computing environments. This project exemplifies the potential of combining advanced telemetry with intelligent data analysis and dynamic optimization to achieve sustainable and high-performance computing.
s






