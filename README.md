# Document-Answering-Robot
### 团队成员 许明乙   詹力闻   张志豪
## 第一周
**需求分析**  
1.功能指标：完成一个能够根据给定内容（wiki上关于deepin系统相关的知识）回答问题的中文聊天机器人，并在博客中记录开发过程中的心得体会，将博客投递到planet.deepin.org

2.性能指标：模型经过训练后需使得回答和问题有80%以上概率的相关性

## 第二周
1.初步了解了pytorch框架以及部分python指令，为后续编程打基础。

2.阅读了部分参考文献，了解了参考文档的形式、问答系统的定义、特点、分类等。查看了部分示例的问答系统，对问答系统的形式有了初步的了解。

## 第三周
1.查阅文献，进一步深入了解问答系统的相关知识。结合现有技术框架，形成了包含数据预处理、模型微调与评估优化的全流程技术方案，已完成初步的路径设计。

2.针对目标领域知识获取需求，已成功利用网络爬虫系统完成指定知识源的原始数据采集，然而在面对数据处理问题时却一筹莫展。为解决数据格式化、加标签等难题，经查阅文献，拟采用**Argilla**开源框架实施数据预处理工程。

3.项目采用三阶段递进式技术路线：
- 数据处理阶段：基于Argilla对参考文档进行处理，实现数据的预处理工作，建立高质量数据库，用于训练与评估。

- 模型训练阶段：使用数据库进行大模型微调训练，并不断评估调优。

- 评估优化阶段：建立包含exact-match、F1-score及语义相似度的多维度评估体系，设计动态参数调优策略
目标设定为在保留测试集上实现问答相关性得分≥80%，达到项目要求。

4.建立起了工程文件，计划后续进一步完善
