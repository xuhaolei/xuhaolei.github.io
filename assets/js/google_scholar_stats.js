(function () {
    var gsDataBaseUrl = 'https://cdn.jsdelivr.net/gh/xuhaolei/xuhaolei.github.io@';
    var cacheBuster = Date.now();
    var primaryUrl = gsDataBaseUrl + "google-scholar-stats/gs_data.json?v=" + cacheBuster;
    var fallbackUrl = 'https://raw.githubusercontent.com/xuhaolei/xuhaolei.github.io/google-scholar-stats/gs_data.json?v=' + cacheBuster;

    function render(data) {
        var citationEles = document.getElementsByClassName('show_paper_citations')
        Array.prototype.forEach.call(citationEles, function (element) {
            var paperId = element.getAttribute('data')
            if (!paperId || !data.publications || !data.publications[paperId]) return;
            var numCitations = data.publications[paperId].num_citations
            element.innerHTML = '| Citations: ' + numCitations;
        });
        var allCitation = document.getElementsByClassName('all_citation_badges')
        Array.prototype.forEach.call(allCitation, function (element) {
            var numCitations = data.citedby
            element.href = 'https://scholar.google.com/citations?user=Wg2cuHUAAAAJ&hl=en'
            element.innerHTML = '<img src="https://img.shields.io/badge/Paper%20Citations-' + numCitations +'-blue?style=social&logo=googlescholar">'
        });
        // Scholar sometimes re-IDs a paper (e.g. after merging versions); fall back
        // to matching the paper title shown next to the badge.
        function normalize(title) {
            return title.toLowerCase().replace(/[^a-z0-9]+/g, '');
        }
        var idByTitle = {};
        Object.keys(data.publications || {}).forEach(function (id) {
            idByTitle[normalize(data.publications[id].bib.title || '')] = id;
        });
        function findPaperId(element) {
            var paperId = element.getAttribute('data');
            if (paperId && data.publications && data.publications[paperId]) return paperId;
            var container = element.closest('p, .paper-box-text');
            var titleEl = container && container.querySelector('strong');
            return titleEl ? idByTitle[normalize(titleEl.textContent)] : null;
        }

        var citationBadges = document.getElementsByClassName('paper_citations_badges')
        Array.prototype.forEach.call(citationBadges, function (element) {
            var paperId = findPaperId(element)
            if (!paperId) return;
            var numCitations = data.publications[paperId].num_citations
            element.href = 'https://scholar.google.com/citations?view_op=view_citation&citation_for_view=' + paperId;
            element.innerHTML = '<img src="https://img.shields.io/badge/citations-' + numCitations +'-blue?style=social&logo=googlescholar">'
        });
    }

    $.getJSON(primaryUrl, render).fail(function () {
        $.getJSON(fallbackUrl, render);
    });
})();
