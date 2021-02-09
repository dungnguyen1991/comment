function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
const csrftoken = getCookie('csrftoken');

$(document).ready(function(){
    $form = $('<form class="mt-3" method="POST" action="/reply/"></form>');
    $form.append("<input type='hidden' name='csrfmiddlewaretoken' value='" + csrftoken + "'>");
    $form.append('<input type="hidden" id="comment" name="comment">');
    $form.append('<textarea name="content" id="" cols="30" rows="5"></textarea>');
    $form.append('<br />');
    $form.append('<input type="button" value="Cancel" class="btn btn-dark me-2 remove-button">');
    $form.append('<input type="submit" value="Post" class="btn btn-primary">');
    $(".reply-button").click(function(){
        $button = $(this);
        $parent = $button.parent();
        $comment_id = $parent.find("#c").val();
        console.log($comment_id);
        $form.find("#comment").val($comment_id);      
        $parent.append($form);
    });

    //gán sự kiện khi sử dụng append một đối tượng sau này
    $(document).on('click', '.remove-button', function(){ 
        $form.remove();
    });
})



