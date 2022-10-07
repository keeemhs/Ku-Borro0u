// 가입부분 체크

function signUpCheck(){

    let password = document.getElementById("password").value
    let passwordCheck = document.getElementById("passwordCheck").value

    // 비밀번호 확인
    if(password !== passwordCheck){
      document.getElementById("passwordError").innerHTML=""
      document.getElementById("passwordCheckError").innerHTML="비밀번호가 동일하지 않습니다."
      check = false
    }else{
      document.getElementById("passwordError").innerHTML=""
      document.getElementById("passwordCheckError").innerHTML=""
    }
  
    if(password===""){
      document.getElementById("passwordError").innerHTML="비밀번호를 입력해주세요."
      check = false
    }else{
      //document.getElementById("passwordError").innerHTML=""
    }
    if(passwordCheck===""){
      document.getElementById("passwordCheckError").innerHTML="비밀번호를 다시 입력해주세요."
      check = false
    }else{
      //document.getElementById("passwordCheckError").innerHTML=""
    }
}