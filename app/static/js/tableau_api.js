var viz;

$(document).ready(function() {
    initializeViz();

    $("#pdf").click(function() {
        exportPDF();
    });
    $("#image").click(function() {
        exportImage();
    });
    $("#crosstab").click(function() {
        exportCrossTab();
    });
    $("#data").click(function() {
        exportData();
    });
    $("#revert").click(function() {
        revertAll();
    });
});

function initializeViz() {
    var placeholderDiv = document.getElementById("tableauViz");
    var url = "https://public.tableau.com/app/profile/robert.williard/viz/PokemonDashboard_17277356141280/Dashboard1";
    var options = {
        width: placeholderDiv.offsetWidth,
        height: placeholderDiv.offsetHeight,
        hideTabs: true,
        hideToolbar: true,
        onFirstInteractive: function() {
            workbook = viz.getWorkbook();
            activeSheet = workbook.getActiveSheet();
        }
    };
    viz = new tableau.Viz(placeholderDiv, url, options);
}

function exportPDF() {
    viz.showExportPDFDialog();
}

function exportImage() {
    viz.showExportImageDialog();
}

function exportCrossTab() {
    viz.showExportCrossTabDialog();
}

function exportData() {
    viz.showExportDataDialog();
}

function revertAll() {
    workbook.revertAllAsync();
}
