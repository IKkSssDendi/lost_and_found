$(function () {
    var lock = false; // 锁定按钮，避免多次点击
    $('.submitResult').click(function () {
        if (lock) {
            return;
        }
        lock = true;
        var vaule = $(this).val()
        var reason;
        data = {
            value: vaule,
        };
        $.ajax({
                type: 'POST',
                url: window.location.href,
                data: data,
                dataType: 'json',
                success: function (res) {
                    if (res.state === 200) {
                        //服务端返回的数据
                        weui.toast(res.msg, 3000);
                        //成功跳转
                        setTimeout(function () {
                            location.reload();
                        }, 2000);
                        // 提交成功删除文本内容，防止重复提交
                        weui.alert(res.msg);
                    } else {
                        // 失败，显示后端信息
                        weui.alert(res.msg);
                    }
                },
                error: function (res) {
                    weui.alert('网络异常，请重试');
                }

            }
        )

    });
});

