$.post("/postdata", function(data){
  data = data.tweets
  for(var i=0;i<data.length;i++){
    var tweetText = data[i].tweet_text;
    var uurl = 'https://twitter.com/search?q=%23INDvSA&src=tyah';
    var sentimentValue = data[i].sentiment;
    $('#tweets-links').append('<a href="' + uurl + '"><div class="article"><h3>' + tweetText + '</h3>'+ sentimentValue +'</div></a><hr><br>' );

  }
});
