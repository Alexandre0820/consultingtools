#!/usr/bin/env python3
"""删除translations中不再使用的企业专区相关i18n键"""

with open('index.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

# 要删除的键（在zh translations中）
keys_to_remove = [
    'enterprise_title',
    'enterprise_subtitle',
    'suwen_ai',
    'suwen_desc',
    'suwen_recommend',
    'suwen_case1',
    'suwen_case2',
    'suwen_case3',
    'suwen_case4',
    'enterprise_platform',
    'platform_desc',
    'platform_recommend',
    'atypica_enterprise_desc',
    'atypica_enterprise_recommend',
    'atypica_case1',
    'atypica_case2',
    'atypica_case3',
    'atypica_case4',
]

new_lines = []
skip = False
skip_count = 0

for i, line in enumerate(lines, 1):
    # 检查是否是要删除的键
    should_skip = any(f'"{key}":' in line for key in keys_to_remove)
    if should_skip:
        skip_count += 1
        continue
    new_lines.append(line)

print(f"删除了 {skip_count} 行")

with open('index.html', 'w', encoding='utf-8') as f:
    f.writelines(new_lines)

print("✅ 清理完成")
