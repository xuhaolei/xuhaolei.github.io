---
permalink: /
title: ""
author_profile: true
redirect_from: 
  - /about/
  - /about.html
---

🌈 I am Haolei Xu (徐皓雷), a second-year PhD student at [Zhejiang University](https://www.zju.edu.cn/english/), College of Computer Science and Technology. Previously, I received my Bachelor's degree from the School of Computer Science, [Harbin Institute of Technology](http://en.hit.edu.cn/).

📌 My research focuses on **LLM Reasoning**, **Reinforcement Learning**, and **Interpretability**.

📢 Feel free to reach out via email: `xuhaolei@zju.edu.cn`.

## 🔥 News

<div class="news-scroll" markdown="1">

* **2026.04** 🎉 One paper has been accepted by **ACL 2026** (Main), about routing distraction in multimodal Mixture-of-Experts ([Seeing but Not Thinking](https://arxiv.org/abs/2604.08541))!
* **2025.09** 🎉 Two papers have been accepted by **NeurIPS 2025**, including [Mind the Gap](https://arxiv.org/abs/2505.14684) about chain-of-thought tuning and [Self-Braking Tuning](https://arxiv.org/abs/2505.14604) about LLM overthinking!
* **2025.09** 📢 [EasySteer](https://arxiv.org/abs/2509.25175) is released, a unified framework for high-performance and extensible LLM Steering! [[code](https://github.com/ZJU-REAL/EasySteer)] [[机器之心](https://mp.weixin.qq.com/s/dxuJHvXOfzA1euvFUPN_vg)]
* **2025.08** 🎉 One paper ([DB-Explore](https://arxiv.org/abs/2503.04959)) about automated database exploration for Text-to-SQL has been accepted by **EMNLP 2025**!
* **2025.07** 🎉 One paper about SVG benchmarking ([SVGenius](https://arxiv.org/abs/2506.03139)) has been accepted by **ACM Multimedia 2025**!
* **2025.04** 📢 A comprehensive survey on (M)LLM-based GUI Agents is released! [[arXiv](https://arxiv.org/abs/2504.13865)] [[code](https://github.com/ZJU-REAL/Awesome-GUI-Agents)]

</div>


## 📝 Publications

Full publications are on my [Google Scholar](https://scholar.google.com/citations?user=Wg2cuHUAAAAJ&hl=en) profile. \*: Equal contribution. †: Project leader. ‡: Corresponding author. <a href="https://scholar.google.com/citations?user=Wg2cuHUAAAAJ" target="_blank"><img src="https://img.shields.io/badge/dynamic/json?label=Paper%20Citations&query=total_citations&url=https%3A%2F%2Fcse.bth.se%2F~fer%2Fgooglescholar-api%2Fgooglescholar.php%3Fuser%3DWg2cuHUAAAAJ&logo=googlescholar&style=social" alt="Google Scholar"></a>

<style>
  .pub-filters {
    display: flex;
    gap: 0.45rem;
    flex-wrap: wrap;
    margin: 1rem 0 0.4rem;
  }

  .pub-filter-btn {
    appearance: none;
    border: 1px solid #00369f;
    border-radius: 4px;
    background: transparent;
    color: #111111;
    cursor: pointer;
    font-size: 0.8rem;
    font-weight: 600;
    line-height: 1.1;
    padding: 0.24rem 0.58rem;
    transition: background-color 0.2s ease, color 0.2s ease, border-color 0.2s ease;
  }

  .pub-filter-btn:hover,
  .pub-filter-btn.is-active {
    background: #00369f;
    border-color: #00369f;
    color: #ffffff;
  }

  .pub-highlight {
    margin: 0 0 1.15rem;
    color: inherit;
    font-size: 0.95rem;
    font-weight: 600;
  }

  .pub-marker {
    display: none;
  }

  .pub-item.is-hidden,
  .pub-section-heading.is-hidden {
    display: none;
  }
</style>

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">ACL 2026</div><img src='images/seeing_but_not_thinking_teaser.png' alt="Seeing but Not Thinking teaser" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[**Seeing but Not Thinking: Routing Distraction in Multimodal Mixture-of-Experts**](https://arxiv.org/abs/2604.08541)

<u>Haolei Xu</u><sup>\*</sup>, Haiwen Hong<sup>\*,†</sup>, Hongxing Li, Rui Zhou, Yang Zhang, Longtao Huang, Hui Xue, Yongliang Shen<sup>‡</sup>, Weiming Lu<sup>‡</sup>, Yueting Zhuang

<div style="display: inline">
  <a href="https://arxiv.org/pdf/2604.08541"><strong>[paper]</strong></a>
</div>

</div>
</div>

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">NeurIPS 2025</div><img src='images/mind_the_gap_teaser.png' alt="Mind the Gap teaser" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[**Mind the Gap: Bridging Thought Leap for Improved Chain-of-Thought Tuning**](https://arxiv.org/abs/2505.14684)

<u>Haolei Xu</u><sup>\*</sup>, Yuchen Yan<sup>\*</sup>, Yongliang Shen<sup>‡</sup>, Wenqi Zhang, Guiyang Hou, Shengpei Jiang, Kaitao Song, Weiming Lu<sup>‡</sup>, Jun Xiao, Yueting Zhuang

<div style="display: inline">
  <a href="https://arxiv.org/pdf/2505.14684"><strong>[paper]</strong></a>
  <a href="https://github.com/ZJU-REAL/Mind-the-Gap"><strong>[code]</strong></a>
  <a href="https://zju-real.github.io/CoT-Bridge/"><strong>[page]</strong></a>
  <a href="https://mp.weixin.qq.com/s/Gjz9CLEGngOBpKRnZ_GC_A"><strong>[机器之心]</strong></a>
  <a href="https://github.com/ZJU-REAL/Mind-the-Gap" target="_blank"><img src="https://img.shields.io/github/stars/ZJU-REAL/Mind-the-Gap?style=social"></a>
</div>

</div>
</div>

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">arXiv</div><img src='images/easysteer_teaser.png' alt="EasySteer teaser" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[**EasySteer: A Unified Framework for High-Performance and Extensible LLM Steering**](https://arxiv.org/abs/2509.25175)

<u>Haolei Xu</u>, Xinyu Mei, Yuchen Yan, Rui Zhou, Wenqi Zhang, Weiming Lu<sup>‡</sup>, Yueting Zhuang, Yongliang Shen<sup>‡</sup>

<div style="display: inline">
  <a href="https://arxiv.org/pdf/2509.25175"><strong>[paper]</strong></a>
  <a href="https://github.com/ZJU-REAL/EasySteer"><strong>[code]</strong></a>
  <a href="https://mp.weixin.qq.com/s/dxuJHvXOfzA1euvFUPN_vg"><strong>[机器之心]</strong></a>
  <a href="https://github.com/ZJU-REAL/EasySteer" target="_blank"><img src="https://img.shields.io/github/stars/ZJU-REAL/EasySteer?style=social"></a>
</div>

</div>
</div>

<div class="pub-filters" id="pub-filters" aria-label="Publication filters">
  <button type="button" class="pub-filter-btn is-active" data-filter="all">All</button>
  <button type="button" class="pub-filter-btn" data-filter="first-author">Core</button>
</div>

<div class="pub-highlight" id="pub-highlight">🚩 Highlight: NeurIPS: 2, ACL: 1, ACM MM: 1, EMNLP: 1.</div>

<script>
  document.addEventListener("DOMContentLoaded", function () {
    var filterRoot = document.getElementById("pub-filters");
    var highlightNode = document.getElementById("pub-highlight");
    if (!filterRoot) return;

    var buttons = Array.prototype.slice.call(filterRoot.querySelectorAll(".pub-filter-btn"));
    var headings = Array.prototype.slice.call(document.querySelectorAll(".pub-section-heading"));
    var highlightOrder = ["NeurIPS", "ACL", "ACMMM", "EMNLP"];
    var sections = headings.map(function (heading) {
      var items = [];
      var current = heading.nextElementSibling;
      while (current) {
        if (current.classList && current.classList.contains("pub-section-heading")) break;
        if (current.tagName === "H2") break;
        if (current.querySelector && current.querySelector(".pub-marker")) {
          current.classList.add("pub-item");
          items.push(current);
        }
        current = current.nextElementSibling;
      }
      return { heading: heading, items: items };
    });

    function getVenue(item) {
      var badge = item.querySelector("a img");
      if (!badge) return null;
      var source = badge.getAttribute("src") || "";
      var match = source.match(/badge\/(NeurIPS|ACL|ACMMM|EMNLP)-/i);
      return match ? match[1] : null;
    }

    function updateHighlight() {
      if (!highlightNode) return;
      var counts = { NeurIPS: 0, ACL: 0, ACMMM: 0, EMNLP: 0 };
      sections.forEach(function (section) {
        section.items.forEach(function (item) {
          if (item.classList.contains("is-hidden")) return;
          var venue = getVenue(item);
          if (venue && Object.prototype.hasOwnProperty.call(counts, venue)) {
            counts[venue] += 1;
          }
        });
      });
      var summary = highlightOrder.filter(function (venue) {
        return counts[venue] > 0;
      }).map(function (venue) {
        var label = venue === "ACMMM" ? "ACM MM" : venue;
        return label + ": " + counts[venue];
      }).join(", ");
      highlightNode.textContent = "🚩 Highlight: " + summary + ".";
    }

    function applyFilter(filter) {
      buttons.forEach(function (button) {
        var isActive = button.getAttribute("data-filter") === filter;
        button.classList.toggle("is-active", isActive);
        button.setAttribute("aria-pressed", isActive ? "true" : "false");
      });
      sections.forEach(function (section) {
        var visibleCount = 0;
        section.items.forEach(function (item) {
          var marker = item.querySelector(".pub-marker");
          var isFirstAuthor = marker && marker.getAttribute("data-first-author") === "true";
          var shouldShow = filter === "all" || isFirstAuthor;
          item.classList.toggle("is-hidden", !shouldShow);
          if (shouldShow) visibleCount += 1;
        });
        section.heading.classList.toggle("is-hidden", visibleCount === 0);
      });
      updateHighlight();
    }

    buttons.forEach(function (button) {
      button.addEventListener("click", function () {
        applyFilter(button.getAttribute("data-filter"));
      });
    });

    applyFilter("all");
  });
</script>

<h3 class="pub-section-heading">Conference Papers</h3>

<a href="https://arxiv.org/abs/2604.08541" target="_blank"><img src="https://img.shields.io/badge/ACL-2026-blue?style=flat-square"></a><span class="pub-marker" data-first-author="true" aria-hidden="true"></span> <u>Haolei Xu</u><sup>\*</sup>, Haiwen Hong<sup>\*,†</sup>, Hongxing Li, Rui Zhou, Yang Zhang, Longtao Huang, Hui Xue, Yongliang Shen<sup>‡</sup>, Weiming Lu<sup>‡</sup>, Yueting Zhuang, &quot;**Seeing but Not Thinking: Routing Distraction in Multimodal Mixture-of-Experts**&quot;. In *Proceedings of the Annual Meeting of the Association for Computational Linguistics (ACL)*, 2026. [[paper](https://arxiv.org/pdf/2604.08541)] <a class="paper_citations_badges" data="Wg2cuHUAAAAJ:LkGwnXOMwfcC" href="" target="_blank"></a>

<a href="https://arxiv.org/abs/2505.14684" target="_blank"><img src="https://img.shields.io/badge/NeurIPS-2025-blue?style=flat-square"></a><span class="pub-marker" data-first-author="true" aria-hidden="true"></span> <u>Haolei Xu</u><sup>\*</sup>, Yuchen Yan<sup>\*</sup>, Yongliang Shen<sup>‡</sup>, Wenqi Zhang, Guiyang Hou, Shengpei Jiang, Kaitao Song, Weiming Lu<sup>‡</sup>, Jun Xiao, Yueting Zhuang, &quot;**Mind the Gap: Bridging Thought Leap for Improved Chain-of-Thought Tuning**&quot;. In *Advances in Neural Information Processing Systems (NeurIPS)*, 2025. [[paper](https://arxiv.org/pdf/2505.14684)] [[code](https://github.com/ZJU-REAL/Mind-the-Gap)] [[page](https://zju-real.github.io/CoT-Bridge/)] [[机器之心](https://mp.weixin.qq.com/s/Gjz9CLEGngOBpKRnZ_GC_A)] <a href="https://github.com/ZJU-REAL/Mind-the-Gap" target="_blank"><img src="https://img.shields.io/github/stars/ZJU-REAL/Mind-the-Gap?style=social"></a> <a class="paper_citations_badges" data="Wg2cuHUAAAAJ:u-x6o8ySG0sC" href="" target="_blank"></a>

<a href="https://arxiv.org/abs/2505.14604" target="_blank"><img src="https://img.shields.io/badge/NeurIPS-2025-blue?style=flat-square"></a><span class="pub-marker" data-first-author="false" aria-hidden="true"></span> Haoran Zhao<sup>\*</sup>, Yuchen Yan<sup>\*</sup>, Yongliang Shen<sup>‡</sup>, <u>Haolei Xu</u>, Wenqi Zhang, Kaitao Song, Jian Shao, Weiming Lu, Jun Xiao, Yueting Zhuang, &quot;**Let LRMs Break Free from Overthinking via Self-Braking Tuning**&quot;. In *Advances in Neural Information Processing Systems (NeurIPS)*, 2025. [[paper](https://arxiv.org/pdf/2505.14604)] [[code](https://github.com/ZJU-REAL/Self-Braking-Tuning)] [[page](https://zju-real.github.io/SBT/)] [[量子位](https://mp.weixin.qq.com/s/3Rkdh6FNF3NK-0lqjgtN5A)] <a href="https://github.com/ZJU-REAL/Self-Braking-Tuning" target="_blank"><img src="https://img.shields.io/github/stars/ZJU-REAL/Self-Braking-Tuning?style=social"></a> <a class="paper_citations_badges" data="Wg2cuHUAAAAJ:ufrVoPGSRksC" href="" target="_blank"></a>

<a href="https://arxiv.org/abs/2506.03139" target="_blank"><img src="https://img.shields.io/badge/ACMMM-2025-blue?style=flat-square"></a><span class="pub-marker" data-first-author="false" aria-hidden="true"></span> Siqi Chen<sup>\*</sup>, Xinyu Dong<sup>\*</sup>, <u>Haolei Xu</u>, Xingyu Wu, Fei Tang, Hang Zhang, Yuchen Yan, Linjuan Wu, Wenqi Zhang, Guiyang Hou, Yongliang Shen, Weiming Lu, Yueting Zhuang, &quot;**SVGenius: Benchmarking LLMs in SVG Understanding, Editing and Generation**&quot;. In *Proceedings of the 33rd ACM International Conference on Multimedia (ACM MM)*, 2025. [[paper](https://arxiv.org/pdf/2506.03139)] [[code](https://github.com/ZJU-REAL/SVGenius)] [[page](https://zju-real.github.io/SVGenius/)] <a href="https://github.com/ZJU-REAL/SVGenius" target="_blank"><img src="https://img.shields.io/github/stars/ZJU-REAL/SVGenius?style=social"></a> <a class="paper_citations_badges" data="Wg2cuHUAAAAJ:YsMSGLbcyi4C" href="" target="_blank"></a>

<a href="https://arxiv.org/abs/2503.04959" target="_blank"><img src="https://img.shields.io/badge/EMNLP-2025-blue?style=flat-square"></a><span class="pub-marker" data-first-author="false" aria-hidden="true"></span> Haoyuan Ma, Yongliang Shen<sup>‡</sup>, Hengwei Liu, Wenqi Zhang, <u>Haolei Xu</u>, Qiuying Peng, Jun Wang, Weiming Lu<sup>‡</sup>, &quot;**DB-Explore: Automated Database Exploration and Instruction Synthesis for Text-to-SQL**&quot;. In *Proceedings of the 2025 Conference on Empirical Methods in Natural Language Processing (EMNLP)*, 2025. [[paper](https://arxiv.org/pdf/2503.04959)] <a class="paper_citations_badges" data="Wg2cuHUAAAAJ:_FxGoFyzp5QC" href="" target="_blank"></a>



<h3 class="pub-section-heading">Preprints & Under Submission</h3>

<a href="https://arxiv.org/abs/2504.13865" target="_blank"><img src="https://img.shields.io/badge/arXiv-2504.13865-B31B1B?style=flat-square"></a><span class="pub-marker" data-first-author="false" aria-hidden="true"></span> Fei Tang<sup>\*</sup>, <u>Haolei Xu</u><sup>\*</sup>, Hang Zhang<sup>\*</sup>, Siqi Chen<sup>\*</sup>, Xingyu Wu<sup>\*</sup>, Yongliang Shen<sup>‡</sup>, Wenqi Zhang, Guiyang Hou, Zeqi Tan, Yuchen Yan, Kaitao Song, Jian Shao, Weiming Lu, Jun Xiao, Yueting Zhuang, &quot;**A Survey on (M)LLM-based GUI Agents**&quot;. *arXiv preprint arXiv:2504.13865*, 2025. [[paper](https://arxiv.org/pdf/2504.13865)] [[code](https://github.com/ZJU-REAL/Awesome-GUI-Agents)] <a href="https://github.com/ZJU-REAL/Awesome-GUI-Agents" target="_blank"><img src="https://img.shields.io/github/stars/ZJU-REAL/Awesome-GUI-Agents?style=social"></a> <a class="paper_citations_badges" data="Wg2cuHUAAAAJ:d1gkVwhDpl0C" href="" target="_blank"></a>

<a href="https://arxiv.org/abs/2509.25175" target="_blank"><img src="https://img.shields.io/badge/arXiv-2509.25175-B31B1B?style=flat-square"></a><span class="pub-marker" data-first-author="true" aria-hidden="true"></span> <u>Haolei Xu</u>, Xinyu Mei, Yuchen Yan, Rui Zhou, Wenqi Zhang, Weiming Lu<sup>‡</sup>, Yueting Zhuang, Yongliang Shen<sup>‡</sup>, &quot;**EasySteer: A Unified Framework for High-Performance and Extensible LLM Steering**&quot;. *arXiv preprint arXiv:2509.25175*, 2025. [[paper](https://arxiv.org/pdf/2509.25175)] [[code](https://github.com/ZJU-REAL/EasySteer)] [[机器之心](https://mp.weixin.qq.com/s/dxuJHvXOfzA1euvFUPN_vg)] <a href="https://github.com/ZJU-REAL/EasySteer" target="_blank"><img src="https://img.shields.io/github/stars/ZJU-REAL/EasySteer?style=social"></a> <a class="paper_citations_badges" data="Wg2cuHUAAAAJ:WF5omc3nYNoC" href="" target="_blank"></a>



## 🎓 Education

* **Ph.D. in Computer Science** — [Zhejiang University](https://www.zju.edu.cn/english/)
  * Time: Sep 2024 – Present.
  * College of Computer Science and Technology.

* **B.S. in Computer Science** — [Harbin Institute of Technology](http://en.hit.edu.cn/)
  * Time: Sep 2020 – Jun 2024.
  * School of Computer Science.



