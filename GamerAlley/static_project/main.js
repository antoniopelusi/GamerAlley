$(document).ready(function () {
    $('#modal-btn').click(function () {
        $('.ui.modal').modal('show')
        ;
    })
})

$(document).ready(
    function () {
        $('#search').hover(
            function () {
                $(this).addClass('Highlight');
            }
            ,
            function () {
                $(this).removeClass('Highlight');
            }
        );
    }
);

$(document).ready(
    function () {
        $('#sendpost').hover(
            function () {
                $(this).addClass('Highlight');
            }
            ,
            function () {
                $(this).removeClass('Highlight');
            }
        );
    }
);

$(document).ready(
    function () {
        $('#new_post').hover(
            function () {
                $(this).addClass('Highlight2');
            }
            ,
            function () {
                $(this).removeClass('Highlight2');
            }
        );
    }
);

$(document).ready(function () {
    let display = false
    $(".cmt_btn").click(function () {
        if (display === false) {
            $(this).next(".comment-box").show("slow");
            display = true
        } else {
            $(this).next(".comment-box").hide("slow");
            display = false
        }
    });
    $('.upvote-form').submit(function (e) {
        e.preventDefault()

        const post_id = $(this).attr('id')

        const upvoteText = $(`.upvote-btn${post_id}`).text()
        const trim = $.trim(upvoteText)

        const url = $(this).attr('action')

        let res;
        const upvotes = $(`.upvote-count${post_id}`).text()
        const trimCount = parseInt(upvotes)

        $.ajax({
            type: 'POST',
            url: url,
            data: {
                'csrfmiddlewaretoken': $('input[name=csrfmiddlewaretoken]').val(),
                'post_id': post_id,
            },
            success: function (response) {
                if (trim === 'Downvote') {
                    $(`.upvote-btn${post_id}`).text('Upvote')
                    res = trimCount - 1
                } else {
                    $(`.upvote-btn${post_id}`).text('Downvote')
                    res = trimCount + 1
                }
                $(`.upvote-count${post_id}`).text(res)
            },

            error: function (response) {
                console.log('error', response)
            }
        })
    })
});

$(document).ready(function () {
    let display = false
    $(".pst_btn").click(function () {
        if (display === false) {
            $(this).next(".post-box").show("slow");
            display = true
        } else {
            $(this).next(".post-box").hide("slow");
            display = false
        }
    });
});

$(document).ready(function () {
    document.getElementById("id_bio").classList.add("darkest");
})

$(document).ready(function () {
    document.getElementById("id_login").classList.add("border");
})

$(document).ready(function () {
    document.getElementById("id_password").classList.add("border");
})

$(document).ready(function () {
    $(".ui.dropdown").dropdown()
})

document.getElementById("id_content").classList.add("darker");
document.getElementById("id_image").classList.add("darker");
document.getElementById("search").classList.add("yellow");
document.getElementById("id_tags").classList.add("ui", "selection", "dropdown", "darker");