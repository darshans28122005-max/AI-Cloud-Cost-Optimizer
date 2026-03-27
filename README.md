\# 🚀 AI-Based Cloud Cost Optimization System



\## 📌 Project Overview

This project automates AWS cloud cost optimization by intelligently monitoring EC2 instances and shutting down idle resources based on CPU utilization.



It helps reduce unnecessary cloud billing by identifying low-usage instances and stopping them automatically.



\---



\## 🔥 Key Features

\- ✅ Automatic EC2 shutdown based on CPU usage (CloudWatch)

\- ✅ Intelligent decision making (CPU < 5%)

\- ✅ AWS Cost Monitoring using Cost Explorer

\- ✅ Email alerts using AWS SNS

\- ✅ Logging system to track activity



\---



\## 🛠️ Technologies Used

\- Python (boto3)

\- AWS EC2

\- AWS CloudWatch

\- AWS SNS

\- AWS Cost Explorer

\- Git \& GitHub



\---



\## ⚙️ How It Works



1\. Fetch all EC2 instances  

2\. Get CPU utilization from CloudWatch  

3\. Identify idle instances (CPU < 5%)  

4\. Stop unused instances automatically  

5\. Send email alert using SNS  

6\. Log activity in a file  

7\. Monitor AWS cost usage  



\---



\## 📂 Project Structure



AI-Cloud-Cost-Optimizer/

├── README.md  

├── ec2\_auto\_shutdown.py  

├── cost\_monitor.py  

├── requirements.txt  



\---



\## 📦 Installation



Install required libraries:



```

pip install -r requirements.txt

```



\---



\## ▶️ Usage



Run EC2 auto shutdown:



```

python ec2\_auto\_shutdown.py

```



Run cost monitoring:



```

python cost\_monitor.py

```



\---



\## 🎯 Outcome



\- Reduced AWS cloud costs  

\- Automated EC2 management  

\- Improved cloud resource efficiency  



\---



\## 🔮 Future Scope



\- AI-based cost prediction  

\- Email/SMS alert enhancements  

\- Web dashboard visualization  



\---



\## 👨‍💻 Author



Darshan S

