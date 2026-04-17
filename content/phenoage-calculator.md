---
title: "PhenoAge 生物学年龄计算器"
description: "基于 Levine 算法，通过 9 项常规血检指标计算您的生物学年龄"
draft: false
---

# 🧬 PhenoAge 生物学年龄计算器

> **算法来源**：Morgan Levine, PhD - Yale University  
> **参考文献**：Levine ME, et al. An epigenetic biomarker of aging for lifespan and healthspan. *Aging*. 2018;10(4):573-591.

---

## ⚠️ 重要声明

> **本计算器结果仅供参考，不作为诊断依据。**  
> 生物学年龄仅反映基于血液指标的生理状态评估，不能替代专业医疗建议。  
> 如有健康问题，请咨询专业医疗人员。

---

## 📝 输入您的血检数据

<div id="phenoage-calculator" style="background: #f7fafc; padding: 30px; border-radius: 10px; margin: 30px 0;">

### 基本信息

| 项目 | 输入 |
|------|------|
| **实际年龄** | <input type="number" id="chronological-age" min="18" max="100" placeholder="岁" style="width: 100px; padding: 8px; margin: 5px;"> 岁 |

### 血检指标（9 项）

| 指标 | 参考范围 | 您的数值 | 单位 |
|------|---------|---------|------|
| **白蛋白 (Albumin)** | 3.5-5.5 | <input type="number" id="albumin" step="0.1" placeholder="4.5" style="width: 100px; padding: 8px;"> | g/dL |
| **肌酐 (Creatinine)** | 0.6-1.2 | <input type="number" id="creatinine" step="0.01" placeholder="0.9" style="width: 100px; padding: 8px;"> | mg/dL |
| **葡萄糖 (Glucose)** | 70-100 | <input type="number" id="glucose" placeholder="90" style="width: 100px; padding: 8px;"> | mg/dL |
| **C 反应蛋白 (CRP)** | 0-3.0 | <input type="number" id="crp" step="0.1" placeholder="1.0" style="width: 100px; padding: 8px;"> | mg/dL |
| **淋巴细胞百分比** | 20-40 | <input type="number" id="lymphocyte" placeholder="30" style="width: 100px; padding: 8px;"> | % |
| **平均红细胞体积 (MCV)** | 80-100 | <input type="number" id="mcv" placeholder="90" style="width: 100px; padding: 8px;"> | fL |
| **红细胞分布宽度 (RDW)** | 11.5-14.5 | <input type="number" id="rdw" step="0.1" placeholder="13.0" style="width: 100px; padding: 8px;"> | % |
| **碱性磷酸酶 (ALP)** | 44-147 | <input type="number" id="alp" placeholder="80" style="width: 100px; padding: 8px;"> | U/L |
| **白细胞计数 (WBC)** | 4.0-11.0 | <input type="number" id="wbc" step="0.1" placeholder="7.0" style="width: 100px; padding: 8px;"> | K/uL |

<div style="margin-top: 30px; text-align: center;">
<button onclick="calculatePhenoAge()" style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); color: white; border: none; padding: 15px 40px; font-size: 18px; border-radius: 8px; cursor: pointer; box-shadow: 0 4px 15px rgba(102, 126, 234, 0.4);">计算生物学年龄</button>
</div>

</div>

---

## 📊 计算结果

<div id="phenoage-result" style="display: none; background: linear-gradient(135deg, #f7fafc 0%, #edf2f7 100%); padding: 30px; border-radius: 10px; margin: 30px 0; border-left: 5px solid #667eea;">

### 您的生物学年龄

<div style="text-align: center; margin: 30px 0;">
<div id="phenoage-display" style="font-size: 72px; font-weight: bold; color: #667eea;">--</div>
<div style="font-size: 24px; color: #718096;">岁</div>
</div>

### 年龄差异

<div style="display: grid; grid-template-columns: 1fr 1fr; gap: 20px; margin: 20px 0;">
<div style="background: white; padding: 20px; border-radius: 8px; text-align: center;">
<div style="font-size: 14px; color: #718096;">实际年龄</div>
<div id="chrono-age-display" style="font-size: 36px; font-weight: bold; color: #2d3748;">--</div>
<div style="font-size: 12px; color: #a0aec0;">岁</div>
</div>
<div style="background: white; padding: 20px; border-radius: 8px; text-align: center;">
<div style="font-size: 14px; color: #718096;">生物学年龄</div>
<div id="bio-age-display" style="font-size: 36px; font-weight: bold; color: #667eea;">--</div>
<div style="font-size: 12px; color: #a0aec0;">岁</div>
</div>
</div>

<div id="age-difference" style="text-align: center; padding: 20px; border-radius: 8px; margin: 20px 0; font-size: 18px; font-weight: bold;">
</div>

### 健康建议

<div id="health-tips" style="background: white; padding: 20px; border-radius: 8px; margin: 20px 0;">
</div>

</div>

---

## 📖 关于 PhenoAge

### 什么是 PhenoAge？

PhenoAge（表型年龄）是由耶鲁大学 Morgan Levine 博士开发的生物学年龄算法。它基于 9 项常规血液检查指标，通过机器学习模型预测个体的生理年龄。

### 算法原理

PhenoAge 算法通过分析以下生理系统的功能状态来评估衰老程度：

1. **肝脏功能** - 白蛋白、碱性磷酸酶
2. **肾脏功能** - 肌酐
3. **代谢状态** - 葡萄糖
4. **炎症水平** - C 反应蛋白、白细胞计数
5. **免疫功能** - 淋巴细胞百分比
6. **造血系统** - 红细胞参数（MCV、RDW）

### 结果解读

| 年龄差异 | 含义 | 建议 |
|---------|------|------|
| **生物年龄 < 实际年龄 -3 岁** | 衰老速度慢 | 保持当前生活方式 |
| **生物年龄 ≈ 实际年龄 ±3 岁** | 正常衰老 | 健康生活方式 |
| **生物年龄 > 实际年龄 +3 岁** | 衰老速度快 | 建议改善生活方式 |

### 参考文献

1. Levine ME, et al. An epigenetic biomarker of aging for lifespan and healthspan. *Aging (Albany NY)*. 2018;10(4):573-591. PMID: [29676998](https://pubmed.ncbi.nlm.nih.gov/29676998/)
2. Levine ME, et al. Development of a DNA methylation biomarker of aging. *Methods Mol Biol*. 2019.

---

## ⚙️ 计算器使用说明

### 如何获取血检数据？

1. **医院体检**：常规体检包含大部分指标
2. **第三方检测机构**：如金域、迪安等
3. **在线预约**：通过阿里健康、京东健康等平台

### 注意事项

- ✅ 空腹抽血（至少 8 小时）
- ✅ 避免剧烈运动后检测
- ✅ 感冒发烧期间不建议检测
- ✅ 使用同一实验室的检测结果

### 数据隐私

- 🔒 所有计算在浏览器本地完成
- 🔒 数据不会上传到服务器
- 🔒 刷新页面后数据自动清除

---

<script>
function calculatePhenoAge() {
    // 获取输入值
    const age = parseFloat(document.getElementById('chronological-age').value);
    const albumin = parseFloat(document.getElementById('albumin').value);
    const creatinine = parseFloat(document.getElementById('creatinine').value);
    const glucose = parseFloat(document.getElementById('glucose').value);
    const crp = parseFloat(document.getElementById('crp').value);
    const lymphocyte = parseFloat(document.getElementById('lymphocyte').value);
    const mcv = parseFloat(document.getElementById('mcv').value);
    const rdw = parseFloat(document.getElementById('rdw').value);
    const alp = parseFloat(document.getElementById('alp').value);
    const wbc = parseFloat(document.getElementById('wbc').value);
    
    // 验证输入
    if (!age || age < 18 || age > 100) {
        alert('请输入有效的年龄（18-100 岁）');
        return;
    }
    
    const requiredFields = [
        {id: 'albumin', name: '白蛋白'},
        {id: 'creatinine', name: '肌酐'},
        {id: 'glucose', name: '葡萄糖'},
        {id: 'crp', name: 'C 反应蛋白'},
        {id: 'lymphocyte', name: '淋巴细胞百分比'},
        {id: 'mcv', name: 'MCV'},
        {id: 'rdw', name: 'RDW'},
        {id: 'alp', name: '碱性磷酸酶'},
        {id: 'wbc', name: '白细胞计数'}
    ];
    
    for (let field of requiredFields) {
        if (!document.getElementById(field.id).value) {
            alert(`请输入${field.name}`);
            return;
        }
    }
    
    // Levine PhenoAge 算法系数（基于 2018 年论文）
    const coefficients = {
        intercept: -7.0207,
        albumin: -0.0340,
        creatinine: 0.0095,
        glucose: 0.0002,
        crp: 0.0954,
        lymphocyte: -0.0130,
        mcv: 0.0095,
        rdw: 0.2217,
        alp: 0.0019,
        wbc: 0.0957,
        age: 0.0956
    };
    
    // 计算线性预测值
    const linearPredictor = coefficients.intercept +
        coefficients.albumin * albumin +
        coefficients.creatinine * creatinine +
        coefficients.glucose * glucose +
        coefficients.crp * crp +
        coefficients.lymphocyte * lymphocyte +
        coefficients.mcv * mcv +
        coefficients.rdw * rdw +
        coefficients.alp * alp +
        coefficients.wbc * wbc +
        coefficients.age * age;
    
    // 转换为 PhenoAge
    const phenoAge = 0.09165 * Math.exp(linearPredictor) + 0.09046 * age + 14.296;
    
    // 显示结果
    document.getElementById('phenoage-calculator').style.display = 'none';
    document.getElementById('phenoage-result').style.display = 'block';
    document.getElementById('phenoage-display').textContent = phenoAge.toFixed(1);
    document.getElementById('chrono-age-display').textContent = age;
    document.getElementById('bio-age-display').textContent = phenoAge.toFixed(1);
    
    // 计算年龄差异
    const ageDiff = phenoAge - age;
    const diffElement = document.getElementById('age-difference');
    
    if (ageDiff < -3) {
        diffElement.style.background = '#c6f6d5';
        diffElement.style.color = '#22543d';
        diffElement.innerHTML = `🎉 您的生物学年龄比实际年龄年轻${Math.abs(ageDiff).toFixed(1)}岁！`;
    } else if (ageDiff < 3) {
        diffElement.style.background = '#feebc8';
        diffElement.style.color = '#744210';
        diffElement.innerHTML = `😊 您的生物学年龄与实际年龄基本一致（差异${ageDiff.toFixed(1)}岁）`;
    } else {
        diffElement.style.background = '#fed7d7';
        diffElement.style.color = '#742a2a';
        diffElement.innerHTML = `⚠️ 您的生物学年龄比实际年龄大${ageDiff.toFixed(1)}岁，建议关注健康`;
    }
    
    // 生成健康建议
    const tipsElement = document.getElementById('health-tips');
    let tips = '<h4 style="margin-top: 0;">个性化健康建议</h4><ul>';
    
    if (crp > 3.0) {
        tips += '<li><strong>降低炎症</strong>：您的 CRP 偏高，建议增加 Omega-3 摄入、规律运动、保证睡眠。</li>';
    }
    
    if (glucose > 100) {
        tips += '<li><strong>血糖管理</strong>：您的血糖偏高，建议控制精制碳水摄入、增加膳食纤维、规律运动。</li>';
    }
    
    if (rdw > 14.5) {
        tips += '<li><strong>营养优化</strong>：您的 RDW 偏高，可能与营养缺乏有关，建议检查铁、B12、叶酸水平。</li>';
    }
    
    if (albumin < 3.5) {
        tips += '<li><strong>蛋白质摄入</strong>：您的白蛋白偏低，建议增加优质蛋白质摄入。</li>';
    }
    
    if (ageDiff > 3) {
        tips += '<li><strong>综合干预</strong>：建议进行全面生活方式评估，包括饮食、运动、睡眠、压力管理。</li>';
        tips += '<li><strong>定期监测</strong>：建议每 3-6 个月复查一次，追踪生物学年龄变化。</li>';
    }
    
    if (tips === '<h4 style="margin-top: 0;">个性化健康建议</h4><ul>') {
        tips += '<li>🎉 您的各项指标良好，继续保持健康的生活方式！</li>';
        tips += '<li>建议每年进行一次全面体检，持续监测健康状态。</li>';
    }
    
    tips += '</ul>';
    tips += '<p style="margin-top: 20px; font-size: 12px; color: #718096;"><strong>免责声明</strong>：本计算器结果仅供参考，不作为诊断依据。具体健康问题请咨询专业医疗人员。</p>';
    
    tipsElement.innerHTML = tips;
    
    // 滚动到结果区域
    document.getElementById('phenoage-result').scrollIntoView({ behavior: 'smooth' });
}
</script>
