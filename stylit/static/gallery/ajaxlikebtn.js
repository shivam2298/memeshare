$('body').on('click','.likebtn',function(e){
          //console.log("clicked");
          e.preventDefault();
          this_ = $(this);
          console.log(this_.attr('href'));
           $.ajax({
      url :this_.attr('href'),
      method : "GET",
      success:function(data){
      if(data.likes===undefined){
      window.open('http://127.0.0.1:8000/accounts/login','_self')
      }else{
      if(data.liked)
      this_.text("unlike");
      else
      this_.text("like");
      this_.append("("+data.likes+")");
      }
      }
      });
      });