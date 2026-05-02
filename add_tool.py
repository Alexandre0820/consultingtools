#!/usr/bin/env python3
import sys

# 读取文件
with open('index.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

# 新工具对象（漂亮缩进）
new_tool = '''                ,
                {
                    "id": "second-brain",
                    "name": "Second Brain",
                    "logo": "assets/logos/second-brain.svg",
                    "category": "数据分析",
                    "description": "LLM自动维护的个人知识库，丢入原始资料即可编译成结构化wiki，适合咨询顾问快速构建知识体系",
                    "description_en": "LLM-maintained personal knowledge base. Drop raw sources and get a structured wiki automatically. Perfect for consultants building knowledge repositories.",
                    "recommendation": "咨询顾问每天处理大量研究报告、竞品分析和客户资料，Second Brain 利用 LLM 自动提取要点、建立交叉引用，将碎片化信息转化为可检索的知识库，极大提升知识整理效率。",
                    "recommendation_en": "Consultants handle massive research reports, competitive analysis, and client materials daily. Second Brain uses LLM to automatically extract key points, create cross-references, and transform fragmented information into a searchable knowledge base, dramatically improving knowledge organization efficiency.",
                    "useCases": [
                        "整理行业研究报告为结构化wiki",
                        "构建竞品分析知识库",
                        "维护个人/团队知识库",
                        "客户交付物的知识管理",
                        "快速生成项目文档库"
                    ],
                    "useCases_en": [
                        "Transform industry research into structured wiki pages",
                        "Build competitive intelligence knowledge base",
                        "Maintain personal/team knowledge repositories",
                        "Knowledge management for client delivers",
                        "Rapidly generate project documentation library"
                    ],
                    "website": "https://github.com/NicholasSpisak/second-brain",
                    "tags": ["知识管理", "Obsidian", "AI自动化", "LLM"]
                }
'''

# 插入位置：在suwen-ai的 '}' 之后，即第538行后
# 我们先找到 "                    }\n" 后面的行，但简单起见，在第538行后插入
insert_after_line = 538  # based on earlier analysis

# 插入
new_lines = lines[:insert_after_line] + [new_tool + '\n'] + lines[insert_after_line:]

# 写回
with open('index.html', 'w', encoding='utf-8') as f:
    f.writelines(new_lines)

print('✅ Second Brain added at line', insert_after_line+1)
