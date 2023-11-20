$(document).ready(function() {
    var table = $('#example').DataTable();
    table.destroy();
    var table = $('#example').DataTable( {
        "ordering": false,
        lengthChange: false,
        buttons: [ 'copy', 'excel', 'pdf', 'colvis' ]
    } );
    
 
    table.buttons().container()
        .appendTo( '#example_wrapper .col-md-6:eq(0)' );

    $('#debit').on('keyup', function(){
        var credit_amt = parseFloat($('#credit').val()) || 0;
        var debit_amt = parseFloat($(this).val()) || 0;
        var balance = credit_amt - debit_amt;
        $('#balance').val(balance.toFixed(2));
    });

    $('.delete').click(function(){
        if (confirm('Want to Delete')){
            var id = $(this).data('del');
            window.location.href = "/delete/"+id;
        }
    });

    $('.edit').click(function(){
        var id = $(this).data('edit');
        window.location.href = "/edit/"+id;
    });

    $('#logout').click(function(){
        history.replaceState({}, document.title, '/logout');
        window.location.reload();
    });

});