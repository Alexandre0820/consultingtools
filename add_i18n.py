#!/usr/bin/env python3
"""
为 enterprise-tools section 添加 data-i18n 属性
"""

import re

# 读取文件
with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 替换素问 AI 卡片的文本为带 data-i18n 的 span
replacements = [
    # 标题
    ('<h3 class="font-heading text-xl font-bold text-gray-900 mb-2">素问 AI</h3>',
     '<h3 class="font-heading text-xl font-bold text-gray-900 mb-2"><span data-i18n="suwen_ai">素问 AI</span></h3>'),

    # 描述
    ('<p class="text-gray-600 text-sm mb-4">\n                            面向医疗健康和生命科学领域的垂直大模型，提供专业的医学知识问答、文献分析、临床决策支持。\n                        </p>',
     '<p class="text-gray-600 text-sm mb-4" data-i18n="suwen_desc">\n                            面向医疗健康和生命科学领域的垂直大模型，提供专业的医学知识问答、文献分析、临床决策支持。\n                        </p>'),

    # 推荐理由
    ('<p class="text-sm text-purple-800">\n                                <strong>推荐理由：</strong>专为医疗行业打造，准确度高，符合医疗合规要求，帮助企业快速应用AI提升研发和临床效率。\n                            </p>',
     '<p class="text-sm text-purple-800" data-i18n="suwen_recommend">\n                                <strong>推荐理由：</strong>专为医疗行业打造，准确度高，符合医疗合规要求，帮助企业快速应用AI提升研发和临床效率。\n                            </p>'),

    # 适用场景标题（已有data-i18n="use_cases"，保持不变）
    # 四个用例
    ('<li class="flex items-start text-sm text-gray-600">\n                                    <svg class="w-4 h-4 text-green-500 mr-2 mt-0.5 flex-shrink-0" fill="currentColor" viewBox="0 0 20 20">\n                                        <path fill-rule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.707-9.293a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z" clip-rule="evenodd"></path>\n                                    </svg>\n                                    医学文献智能分析\n                                </li>',
     '<li class="flex items-start text-sm text-gray-600">\n                                    <svg class="w-4 h-4 text-green-500 mr-2 mt-0.5 flex-shrink-0" fill="currentColor" viewBox="0 0 20 20">\n                                        <path fill-rule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.707-9.293a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z" clip-rule="evenodd"></path>\n                                    </svg>\n                                    <span data-i18n="suwen_case1">医学文献智能分析</span>\n                                </li>'),

    ('<li class="flex items-start text-sm text-gray-600">\n                                    <svg class="w-4 h-4 text-green-500 mr-2 mt-0.5 flex-shrink-0" fill="currentColor" viewBox="0 0 20 20">\n                                        <path fill-rule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.707-9.293a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z" clip-rule="evenodd"></path>\n                                    </svg>\n                                    临床试验数据解读\n                                </li>',
     '<li class="flex items-start text-sm text-gray-600">\n                                    <svg class="w-4 h-4 text-green-500 mr-2 mt-0.5 flex-shrink-0" fill="currentColor" viewBox="0 0 20 20">\n                                        <path fill-rule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.707-9.293a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z" clip-rule="evenodd"></path>\n                                    </svg>\n                                    <span data-i18n="suwen_case2">临床试验数据解读</span>\n                                </li>'),

    ('<li class="flex items-start text-sm text-gray-600">\n                                    <svg class="w-4 h-4 text-green-500 mr-2 mt-0.5 flex-shrink-0" fill="currentColor" viewBox="0 0 20 20">\n                                        <path fill-rule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.707-9.293a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z" clip-rule="evenodd"></path>\n                                    </svg>\n                                    医疗知识问答系统\n                                </li>',
     '<li class="flex items-start text-sm text-gray-600">\n                                    <svg class="w-4 h-4 text-green-500 mr-2 mt-0.5 flex-shrink-0" fill="currentColor" viewBox="0 0 20 20">\n                                        <path fill-rule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.707-9.293a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z" clip-rule="evenodd"></path>\n                                    </svg>\n                                    <span data-i18n="suwen_case3">医疗知识问答系统</span>\n                                </li>'),

    ('<li class="flex items-start text-sm text-gray-600">\n                                    <svg class="w-4 h-4 text-green-500 mr-2 mt-0.5 flex-shrink-0" fill="currentColor" viewBox="0 0 20 20">\n                                        <path fill-rule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.707-9.293a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z" clip-rule="evenodd"></path>\n                                    </svg>\n                                    药物研发智能辅助\n                                </li>',
     '<li class="flex items-start text-sm text-gray-600">\n                                    <svg class="w-4 h-4 text-green-500 mr-2 mt-0.5 flex-shrink-0" fill="currentColor" viewBox="0 0 20 20">\n                                        <path fill-rule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.707-9.293a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z" clip-rule="evenodd"></path>\n                                    </svg>\n                                    <span data-i18n="suwen_case4">药物研发智能辅助</span>\n                                </li>'),
]

for old, new in replacements:
    if old in content:
        content = content.replace(old, new)
        print(f"✓ Replaced pattern")
    else:
        print(f"✗ Pattern not found")

# 同样为企业AI平台卡片添加 data-i18n
content = content.replace(
    '<h3 class="font-heading text-xl font-bold text-gray-900 mb-2">企业AI平台</h3>',
    '<h3 class="font-heading text-xl font-bold text-gray-900 mb-2"><span data-i18n="enterprise_platform">企业AI平台</span></h3>'
)

content = content.replace(
    '<p class="text-gray-600 text-sm mb-4">\n                            一体化企业级AI中台，整合大模型能力，为企业提供可落地的AI解决方案。\n                        </p>',
    '<p class="text-gray-600 text-sm mb-4" data-i18n="platform_desc">\n                            一体化企业级AI中台，整合大模型能力，为企业提供可落地的AI解决方案。\n                        </p>'
)

content = content.replace(
    '<p class="text-sm text-blue-800">\n                                <strong>推荐理由：</strong>帮助企业快速构建AI能力，降低部署成本，支持私有化部署保障数据安全。\n                            </p>',
    '<p class="text-sm text-blue-800" data-i18n="platform_recommend">\n                                <strong>推荐理由：</strong>帮助企业快速构建AI能力，降低部署成本，支持私有化部署保障数据安全。\n                            </p>'
)

# 为服务卡片标题和描述添加data-i18n（enterprise-cta section）
content = content.replace(
    '<h3 class="text-xl font-bold mb-2">AI 转型陪跑</h3>',
    '<h3 class="text-xl font-bold mb-2"><span data-i18n="service1_title">AI 转型陪跑</span></h3>'
)
content = content.replace(
    '<p class="text-gray-300 text-sm">\n                        从战略规划到落地实施，全程陪伴企业完成 AI 转型与流程变革，确保转型成功。\n                    </p>',
    '<p class="text-gray-300 text-sm" data-i18n="service1_desc">\n                        从战略规划到落地实施，全程陪伴企业完成 AI 转型与流程变革，确保转型成功。\n                    </p>'
)

content = content.replace(
    '<h3 class="text-xl font-bold mb-2">定义人机边界</h3>',
    '<h3 class="text-xl font-bold mb-2"><span data-i18n="service2_title">定义人机边界</span></h3>'
)
content = content.replace(
    '<p class="text-gray-300 text-sm">\n                        科学规划 AI 与人类的协作模式，明确职责分工，最大化人机协同效率。\n                    </p>',
    '<p class="text-gray-300 text-sm" data-i18n="service2_desc">\n                        科学规划 AI 与人类的协作模式，明确职责分工，最大化人机协同效率。\n                    </p>'
)

content = content.replace(
    '<h3 class="text-xl font-bold mb-2">员工技能提升</h3>',
    '<h3 class="text-xl font-bold mb-2"><span data-i18n="service3_title">员工技能提升</span></h3>'
)
content = content.replace(
    '<p class="text-gray-300 text-sm">\n                        系统性培训员工 AI 技能，从基础使用到高级应用，打造企业 AI 人才梯队。\n                    </p>',
    '<p class="text-gray-300 text-sm" data-i18n="service3_desc">\n                        系统性培训员工 AI 技能，从基础使用到高级应用，打造企业 AI 人才梯队。\n                    </p>'
)

# 更新setLanguage函数中的逻辑，处理带data-i18n的span
old_setlang = '''            // Update all elements with data-i18n attribute
            document.querySelectorAll('[data-i18n]').forEach(el => {
                const key = el.getAttribute('data-i18n');
                if (translations[lang][key]) {
                    el.innerHTML = translations[lang][key];
                }
            });'''

new_setlang = '''            // Update all elements with data-i18n attribute
            document.querySelectorAll('[data-i18n]').forEach(el => {
                const key = el.getAttribute('data-i18n');
                if (translations[lang][key]) {
                    el.innerHTML = translations[lang][key];
                }
            });
            // Update elements with span[data-i18n] inside headings
            document.querySelectorAll('h3[data-i18n], h3 span[data-i18n], h2[data-i18n], h2 span[data-i18n]').forEach(el => {
                const key = el.getAttribute('data-i18n');
                if (translations[lang][key]) {
                    el.innerHTML = translations[lang][key];
                }
            });'''

content = content.replace(old_setlang, new_setlang)

# 保存文件
with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("✅ 已添加 data-i18n 属性并更新 setLanguage 逻辑")
