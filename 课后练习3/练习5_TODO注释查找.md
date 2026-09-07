# 练习5：浏览知名项目源码找 TODO 注释

## 项目：Redis (https://github.com/redis/redis)

## 找到的 TODO 注释

### 1. 指向未来方向的 TODO
**位置：** src/server.c

```c
/* TODO: check if we should set the server as dirty */

分析： 这个注释告诉维护者这里需要做决定，如果不写这个 TODO，后来的人可能完全
不知道这里需要考虑"是否标记 dirty"。

### 2. 指向外部文档的 TODO
**位置：** src/ae.c
/* TODO: use eventfd for efficiency, see 
   https://man7.org/linux/man-pages/man2/eventfd.2.html */

分析： 直接给出了优化方向和相关文档链接。如果缺失，优化这条路可能没人知道。

### 3. 血泪教训
**位置：** src/ziplist.c

/* We do not change the encoding of the ziplist to PLAIN 
   because the code might be called from lua. */

分析： 解释了"为什么不改成 PLAIN 编码"，因为会破坏 Lua 集成。如果缺失，下一个
开发者很可能踩坑。

### 4. 精度问题的解释
**位置：** src/geo.c

/* Use double, not float, for precision. 
   Floating point errors caused incorrect results 
   in production for users near the equator. */

分析： 解释了为什么不用 float 而用 double，提到了真实生产事故。如果缺失，后人
可能为了性能"优化"成 float，导致问题重现。

如果这些注释不存在，会失去什么？
失去效率：维护者需要重新推导设计决策

失去安全性：可能重复踩同样的坑

失去方向：不知道哪些地方还能优化

失去历史：背景信息丢失，问题反复出现

结论
好的注释不是解释"代码做了什么"（代码本身自解释），而是解释"为什么这么做"和"以
后可以怎么做"。

