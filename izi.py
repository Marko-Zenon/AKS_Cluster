import matplotlib.pyplot as plt
import numpy as np

# Налаштування стилю
plt.rcParams.update({'font.size': 12, 'axes.facecolor': '#f9f9f9'})

# Данні для Qwen-2.5-32B
nodes = ['Node 1 (Master)', 'Node 2 (Worker)', 'Node 3 (Worker)', 'Node 4 (Worker)']
ram_used_gb = [0.76, 6.35, 6.32, 6.37]  # GiB
cpu_load_per_worker = 20.0 # % (середнє з Load AVG)

net_labels = ['Node 1', 'Node 2', 'Node 3', 'Node 4']
# Вхідний трафік (GiB)
download_gb = [0.12, 22.6, 22.6, 23.1]
# Вихідний трафік (GiB)
upload_gb = [16.3, 0.24, 0.24, 0.47]

# --- ГРАФІК 1: Розподіл RAM (Heavy Load) ---
plt.figure(figsize=(10, 6))
bars = plt.bar(nodes, ram_used_gb, color=['#4CAF50', '#673AB7', '#673AB7', '#673AB7'], edgecolor='black', alpha=0.9)
plt.title('RAM Usage: Start Qwen-2.5-32B (Q5)', fontsize=16, fontweight='bold', pad=20)
plt.ylabel('RAM Used (GiB)', fontsize=12)
plt.ylim(0, 8)  # Limit to 8GB
for bar in bars:
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2., height + 0.1, f'{height} GiB', ha='center', va='bottom', fontweight='bold')
plt.grid(axis='y', linestyle='--', alpha=0.5)
plt.tight_layout()
plt.savefig('ram_heavy_final.png', dpi=300)

# --- ГРАФІК 2: Мережевий трафік (Heavy Load) ---
x = np.arange(len(net_labels))
width = 0.35
plt.figure(figsize=(10, 6))
plt.bar(x - width/2, download_gb, width, label='Download (Вхідний)', color='#E91E63', edgecolor='black', alpha=0.9)
plt.bar(x + width/2, upload_gb, width, label='Upload (Віддача)', color='#FF9800', edgecolor='black', alpha=0.9)
plt.title('Network Activity under Heavy Load', fontsize=16, fontweight='bold', pad=20)
plt.xticks(x, net_labels)
plt.ylabel('Data Volume (GiB)', fontsize=12)
plt.legend()
plt.grid(axis='y', linestyle='--', alpha=0.5)
plt.tight_layout()
plt.savefig('network_heavy_final.png', dpi=300)

# --- ГРАФІК 3: Продуктивність (Speed) ---
perf_labels = ['Llama-3-8B', 'Qwen-2.5-32B']
# t/s взято прямо з терміналів
perf_values = [1.7, 0.5] 

plt.figure(figsize=(8, 6))
bars3 = plt.bar(perf_labels, perf_values, color=['#2196F3', '#FFC107'], edgecolor='black', width=0.6)
plt.title('Performance Comparison: Light vs Heavy Model', fontsize=16, fontweight='bold', pad=20)
plt.ylabel('Tokens per Second (t/s)', fontsize=12)
plt.ylim(0, 2.0)
for bar in bars3:
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2., height + 0.05, f'{height} t/s', ha='center', va='bottom', fontweight='bold', fontsize=14)
plt.tight_layout()
plt.savefig('performance_heavy_final.png', dpi=300)

print("Всі 3 важкі графіки згенеровані!")