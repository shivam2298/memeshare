$('.comment_form').on('submit',function(event){
    event.preventDefault();
    console.log("inside form call");
    var this_ = $(this);
    var id = this_.attr("id");
    url = '/gallery/'+id+'/comment/';
    var data = $('#meme').val();
    var csrf  =  this_.find('input[name="csrfmiddlewaretoken"]').val();
    console.log(data,id);
    $.ajax({
    url : url,

    data :{'comment':data,'csrfmiddlewaretoken':csrf},
    method : "POST",
    success:function(data){
    if(data.added==0)
    window.open('http://127.0.0.1:8000/accounts/login','_self');
    else
    $('#box').append("<li class='list-group-item d-flex justify-content-between align-items-center'>"+
    data.comment+"<span><a href='/accounts/"+data.username+"/portfolio/'>"+data.username+"</a> </span></li>");
    },
    error:function(data){
    console.log("error");
    }
    });
    });