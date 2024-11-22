以下是为你的 GitHub 仓库 `https://github.com/notajely/assignment_2_5LN715` 编写的 **README** 文件内容：

---

# **Assignment 2 - Advanced Programming (5LN715)**

## **项目简介**

本项目是乌普萨拉大学 **Advanced Programming (5LN715)** 课程的第二次作业。旨在研究语音清晰度与信息量（Surprisal）之间的关系，通过分析语音持续时长和语言信息量，验证语音清晰度与信息量成正相关的假设。

---

## **任务目标**

1. **数据处理** ：

* 使用 `wiki.train.raw` 数据训练双词模型（Bigram Model）。
* 提取 `wiki.test.raw` 数据的信息量并生成句子 Surprisal 值。

2. **语音数据采集** ：

* 录制与测试句子对应的语音数据。
* 使用 **MAUS（Munich Automatic Segmentation System）** 提取音素的持续时长。

3. **分析与建模** ：

* 使用线性回归模型，探索语音清晰度（时长）与信息量（Surprisal）之间的关系。
* 使用直方图和回归图进行数据可视化。

4. **学习目标** ：

* 掌握模块化编程、数据处理与分析技能。
* 熟悉语音与文本数据处理工具，如 MAUS 和 Python 的数据科学库。

---

## **文件结构**

项目文件结构说明如下：

```plaintext
assignment_2_5LN715/
│
├── data/                           # 数据目录
│   ├── external/                   # 原始数据：wiki.train.raw, wiki.test.raw
│   ├── processed/                  # 处理后的数据：data.csv
│   ├── recordings/                 # 录音文件（仅本地存储，不提交）
│
├── scripts/                        # 核心 Python 脚本
│   ├── get_durations.py            # 从 MAUS 输出提取语音时长
│   ├── get_surprisals.py           # 计算信息量
│   ├── get_linear_model.py         # 构建线性回归模型
│   ├── get_histogram.py            # 生成语音时长直方图
│
├── results/                        # 分析结果目录
│   ├── plots/                      # 可视化结果：直方图与回归图
│   ├── models/                     # 保存的回归模型文件
│
├── README.md                       # 项目说明文件
├── requirements.txt                # Python 依赖清单
├── .gitignore                      # 忽略提交的文件配置
```

---

## **安装与运行**

### **环境依赖**

1. **安装 Python 及依赖库** ：
   确保 Python 版本为 3.8+，并通过以下命令安装依赖：

```bash
   pip install -r requirements.txt
```

2. **安装其他工具** ：

* **MAUS** ：用于处理语音数据。
* **Praat** ：用于验证语音时长计算结果。
* **ffmpeg 或 sox** ：用于音频格式转换。

### **运行步骤**

1. **计算信息量** ：
   使用 `scripts/get_surprisals.py` 提取测试句子的 Surprisal 值。
2. **录制语音** ：

* 录制测试句子的音频，存储为 `data/recordings/`。
* 使用 MAUS 处理音频并生成语音时长文件。

3. **数据处理与分析** ：

* 使用 `scripts/get_durations.py` 计算单词时长。
* 使用 `scripts/get_linear_model.py` 构建线性回归模型。
* 使用 `scripts/get_histogram.py` 可视化时长分布。

---

## **功能说明**

1. **get_durations.py** ：

* 提取 MAUS 输出中的语音时长，输出格式为字典。

2. **get_surprisals.py** ：

* 训练双词模型（Bigram Model）。
* 计算句子的平均 Surprisal。

3. **get_linear_model.py** ：

* 使用 Pandas 和 Scikit-learn 构建线性回归模型。
* 输出回归系数、p 值、R² 值等统计结果。

4. **get_histogram.py** ：

* 绘制语音时长分布的直方图，用于展示数据特性。

---

## **示例输出**

### **线性回归模型结果** ：

* 回归系数：`0.52`
* 截距：`1.25`
* R² 值：`0.76`
* p 值：`< 0.001`

### **可视化图表** ：

1. 语音时长直方图
2. 信息量与时长的回归散点图

---

## **未来扩展**

1. 使用更复杂的语言模型（如 GPT 或 Huggingface Transformers）计算信息量。
2. 探讨其他语言或语料库在类似研究中的表现。
3. 将 POS（词性）标签引入分析，探索功能词和内容词的不同模式。

---

## **参考文献**

1. Jaeger, T. F., & Buz, E. (2017). Signal reduction and linguistic encoding.  *The Handbook of Psycholinguistics* .
2. Kisler, T., Reichel, U., & Schiel, F. (2017). Multilingual processing of speech via web services.  *Computer Speech & Language* .

---

### **仓库链接**

GitHub: [assignment_2_5LN715](https://github.com/notajely/assignment_2_5LN715)
