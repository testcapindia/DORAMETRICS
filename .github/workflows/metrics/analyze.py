#!/usr/bin/env python3
import csv
from datetime import datetime
from collections import defaultdict

def analyze_metrics():
    with open('metrics/dora-data.csv', 'r') as f:
        reader = csv.DictReader(f)
        data = list(reader)
    
    deployments = [d for d in data if d['Event'] == 'deployment']
    incidents = [d for d in data if d['Event'] == 'incident']
    
    # Calculate metrics
    total_deps = len(deployments)
    failed_deps = len([d for d in deployments if d['Success'] == 'false'])
    lead_times = [float(d['Lead_Time_Hours']) for d in deployments]
    mttrs = [float(i['Lead_Time_Hours']) for i in incidents]
    
    avg_lead_time = sum(lead_times) / len(lead_times)
    failure_rate = (failed_deps / total_deps * 100) if total_deps else 0
    avg_mttr = sum(mttrs) / len(mttrs) if mttrs else 0
    deploy_freq = total_deps / 90  # 3 months
    
    # Monthly breakdown
    monthly = defaultdict(lambda: {'deps': 0, 'failures': 0, 'incidents': 0})
    for d in deployments:
        month = d['Date'][:7]
        monthly[month]['deps'] += 1
        if d['Success'] == 'false':
            monthly[month]['failures'] += 1
    
    for i in incidents:
        month = i['Date'][:7]
        monthly[month]['incidents'] += 1
    
    # Print report
    print("="*70)
    print("📊 DORA METRICS REPORT - 3 MONTHS (Sept-Dec 2024)")
    print("="*70)
    print(f"\n🚀 DEPLOYMENT FREQUENCY")
    print(f"   Total Deployments: {total_deps}")
    print(f"   Per Day: {deploy_freq:.2f}")
    print(f"   Performance: {'Elite 🏆' if deploy_freq >= 1 else 'High 🥈' if deploy_freq >= 0.14 else 'Medium 🥉'}")
    
    print(f"\n⏱️  LEAD TIME FOR CHANGES")
    print(f"   Average: {avg_lead_time:.1f} hours")
    print(f"   Min: {min(lead_times):.0f}h | Max: {max(lead_times):.0f}h")
    print(f"   Performance: {'Elite 🏆' if avg_lead_time <= 24 else 'High 🥈' if avg_lead_time <= 168 else 'Medium 🥉'}")
    
    print(f"\n❌ CHANGE FAILURE RATE")
    print(f"   Failed: {failed_deps}/{total_deps}")
    print(f"   Rate: {failure_rate:.2f}%")
    print(f"   Performance: {'Elite 🏆' if failure_rate <= 5 else 'High 🥈' if failure_rate <= 10 else 'Medium 🥉'}")
    
    print(f"\n🔧 TIME TO RESTORE SERVICE")
    print(f"   Total Incidents: {len(incidents)}")
    print(f"   Average MTTR: {avg_mttr:.1f} hours")
    print(f"   Performance: {'Elite 🏆' if avg_mttr <= 1 else 'High 🥈' if avg_mttr <= 24 else 'Medium 🥉'}")
    
    print(f"\n📅 MONTHLY BREAKDOWN")
    print(f"   {'Month':<12} {'Deployments':<15} {'Failures':<12} {'Incidents':<12}")
    print(f"   {'-'*51}")
    for month in sorted(monthly.keys()):
        m = monthly[month]
        print(f"   {month:<12} {m['deps']:<15} {m['failures']:<12} {m['incidents']:<12}")
    
    print("\n" + "="*70)

if __name__ == '__main__':
    analyze_metrics()
