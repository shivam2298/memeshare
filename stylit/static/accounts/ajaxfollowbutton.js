$('body').on('click','.followbtn',function(e){
          //console.log("clicked");
          e.preventDefault();
          this_ = $(this);
          console.log(this_.attr('href'));
           $.ajax({
      url :this_.attr('href'),
      method : "GET",
      success:function(data){
      if(data.notlogedin===true){
      window.open('http://127.0.0.1:8000/accounts/login','_self');
      }else{
      if(data.followed)
      this_.text("Unfollow");
      else
      this_.text("follow");
      $('.following').text(data.following);
      $('.followers').text(data.followers);
      }
      }
      });
      });