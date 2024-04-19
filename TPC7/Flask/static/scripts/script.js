function delete_conceito(designacao){
    $.ajax({
        url:'/conceitos/' + designacao,
        type: 'DELETE',
        success: function (result) {
            window.location.href="/conceitos"
        }
    });
}

$(document).ready( function () {
    $('#myTable').DataTable();
} );