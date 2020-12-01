$(function () {

    $(".js-criar-livro").click(function () {
      $.ajax({
        url: '/livros/cria/',
        type: 'get',
        dataType: 'json',
        beforeSend: function () {
          $("#modal-book").modal("show");
        },
        success: function (data) {
          $("#modal-book .modal-content").html(data.html_form);
        }
      });
    });
  
  });