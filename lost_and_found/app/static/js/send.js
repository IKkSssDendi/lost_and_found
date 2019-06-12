$(function () {
    var lock = false; // 锁定按钮，避免多次点击
    $('.submitBtn').click(function () {
        if (lock) {
            return;
        }
        lock = true;
        var state = $('.state').is(":checked");
        var article_name = $('#article').val().replace(/\s+/g, '');
        var receive_name = $('#receive_name').val().replace(/\s+/g, '');
        var send_name = $('#send_name').val().replace(/\s+/g, '');
        var content = $('#content').val().replace(/(^\s*)|(\s*$)/g, '');
        var is_show_head = $('#is_show_head').is(":checked");
        var reason;
        //验证表单合法性
        if (!state) {
            reason = "请选择丢失物品/拾取物品";
        }
        else if (!article_name) {
            reason = "请输入物品名称";
        }
         else if (!send_name) {
            reason = "请输入你的姓名";
        } else if (!content) {
            reason = "请输入丢失/拾取物品描述内容";
        } else if (content.length < 10) {
            reason = "描述内容过短，请再输入一些吧";
        }

        if (reason) {
            weui.alert(reason);
            lock = false;
            return;
        }
        data = {
            status:state,
            article_name:article_name,
            receive_name: receive_name,
            send_name: send_name,
            content: content,
            is_show_head: is_show_head
        };
        $.ajax({
                type: 'POST',
                url: window.location.href,
                data: data,
                dataType: 'json',
                success: function (res) {
                    //这里面基本不用改
                    if (res.state === 200) {
                        //服务端返回的数据
                        weui.toast(res.msg, 3000);
                        //成功跳转
                        setTimeout(function () {
                            $('top-button').trigger("click");
                        }, 3000);
                        // 提交成功删除文本内容，防止重复提交
                        $('.reset').trigger("click");
                    } else {
                        // 失败，显示后端信息
                        weui.alert(res.msg);
                    }
                },
                error: function (res) {
                    weui.alert('网络异常，请重试');
                },
                //这里应该可以不用写
                //complete: function (res) {
                //    loading.hide();
                //    lock = false;
                //    console.log("finished",res);
                //
                //},

            }
        )

    });
});
