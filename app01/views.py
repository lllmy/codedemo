from django.shortcuts import render,redirect

# Create your views here.


def upload(request):
    if request.method == "POST":
        file_obj = request.FILES.get("file")
        with open(file_obj.name, "wb") as f:
            for chunk in file_obj.chunks():
                f.write(chunk)
            # 已经将文件保存在服务端，现在开始进行代码统计
        code_line = 0
        comment_line = 0
        flag = False
        with open(file_obj.name, "r", encoding="utf-8") as f2:
            for line in f2:
                if line.strip():
                    if flag and not line.strip().startswith('"""'):
                        comment_line += 1
                    else:
                        if line.strip().startswith("#"):
                            comment_line += 1
                        elif line.strip().startswith('"""'):
                            if not flag:
                                flag = True
                            else:
                                flag = False
                            comment_line += 1
                        else:
                            code_line += 1
        return render(request, "show.html", {"filename": file_obj.name, "code_line": code_line, "comment_line": comment_line})
    return render(request, "upload.html")