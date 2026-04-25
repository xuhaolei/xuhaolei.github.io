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
        var citationBadges = document.getElementsByClassName('paper_citations_badges')
        Array.prototype.forEach.call(citationBadges, function (element) {
            var paperId = element.getAttribute('data')
            if (!paperId || !data.publications || !data.publications[paperId]) return;
            var numCitations = data.publications[paperId].num_citations
            element.href = 'https://scholar.google.com/citations?view_op=view_citation&citation_for_view=' + paperId;
            element.innerHTML = '<img src="https://img.shields.io/badge/citations-' + numCitations +'-blue?style=social&logo=googlescholar">'
        });
    }

    $.getJSON(primaryUrl, render).fail(function () {
        $.getJSON(fallbackUrl, render);
    });
})();
