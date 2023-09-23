## Project 03-02

直方图均衡化

- 修正：注意公式 $T(r_k)=(L-1)\sum\limits_{j=0}^k \frac{n_j}{MN}$ 中对灰度值 count 的前缀累加，包括本灰度值 $r_k$ 对应的频数 $n_k$，在写循环时注意终止条件。
- 
  