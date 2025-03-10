# 文件夹说明

显存优化技术论文：
- Swap：内存交换 (memory swapping) 或卸载 (offload) 
- Recomp：激活重计算 (activation recomputation) 或梯度检查点 (gradient checkpointing) 或再物化（rematerialization）
- Hybrid：内存交换与重计算的混合策略
- MAS：内存分配策略 (memory allocation strategies) 

注：部分 Swap、Recomp 和 Hybrid 中的论文可能还包含内存复用 (memory reuse) 和内存池 (memory pooling) 等内存分配策略，但为了区分，不再将这类论文添加进 MAS 文件夹。读者可以参考表格 InfoSummary.xlsx 中的“分类”列，对论文作进一步区分。

其它论文：

- 框架：深度学习框架、分布式训练框架、ZeRO 系列
- 模型：CNN、Transformer、LLM 模型
- 综述：MLSys_GPU_Memory_Opt 相关