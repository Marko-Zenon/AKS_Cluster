# Distributed LLM Cluster on Radxa Dragon-Q6A

This project demonstrates the construction and benchmarking of a high-performance computing cluster using four **Radxa Dragon-Q6A** single-board computers. We utilized the `llama.cpp` RPC (Remote Procedure Call) backend to perform distributed inference of the **Llama-3-8B** model.

## 🚀 Overview
The primary goal of this project was to overcome the memory limitations of individual SBCs. By pooling the RAM of 4 nodes, we successfully deployed a large language model that would otherwise be impossible to run on a single 8GB board.

## 🛠 Hardware Configuration
* **Nodes:** 4x Radxa Dragon-Q6A (Rockchip SoC, 8GB RAM each)
* **Interconnect:** Gigabit Ethernet Switch
* **Total Cluster RAM:** 32 GB

## 💻 Software Stack
* **OS:** Radxa OS (Linux)
* **Inference Engine:** `llama.cpp` with RPC support
* **Model:** Llama-3-8B-Instruct (Quantization: Q8_0)
* **Monitoring:** `btop`, `tmux`

## 📊 Performance Analysis

### 1. Generation Speed (Tokens per Second)
On a single node, Llama-3-8B (8.5 GB) causes heavy disk swapping, resulting in unusable performance (~0.4 t/s). Our cluster setup achieved a stable **1.7 t/s**, providing a 4x performance boost and a smooth user experience.

![Performance Comparison](./performance_t_s.png)

### 2. RAM Distribution
We implemented **Model Parallelism**. The model weights were partitioned across the worker nodes, ensuring that no single node exceeded its physical memory limit.

| Node | Role | RAM Usage |
| :--- | :--- | :--- |
| Node 1 | Master / Orchestrator | ~0.56 GiB |
| Node 2 | RPC Worker | ~3.42 GiB |
| Node 3 | RPC Worker | ~3.42 GiB |
| Node 4 | RPC Worker | ~3.69 GiB |

![RAM Usage Distribution](./ram_usage_final.png)

### 3. Network Traffic
The Master node acts as the initial data source, uploading the model parts to the workers. During inference, nodes exchange small tensors representing intermediate calculations.

![Network Traffic](./network_usage_final.png)

## 📸 Terminal Screenshots
Below are the monitoring logs from our session:

### Master Node (Node 1)
![Master Node Terminal](./1_нода.jpg)
*Running `llama-cli` and orchestrating the cluster.*

### Worker Node (Typical)
![Worker Node Terminal](./2_нода.jpg)
*Running `rpc-server` and processing model layers.*

## ⚠️ Challenges & Solutions
1. **Power Management:** Boards were entering sleep mode. Fixed by masking `suspend.target` and setting the CPU governor to `performance`.
2. **Thermal Issues:** Intensive LLM workloads caused throttling. Solved by installing active cooling (fans) on all nodes.
3. **RPC Synchronization:** Version mismatch in `llama.cpp` binaries caused connection drops. Solved by rebuilding the project from source across all nodes simultaneously.

## 🏁 Conclusion
This setup proves that SBC clusters are a viable and cost-effective solution for running private, localized LLMs. Through distributed computing, we achieved usable performance for a state-of-the-art 8B parameter model on low-power hardware.
