const commentButton = document.querySelector('.comment_button');
const commentList = document.querySelector('.comment');
const form = document.getElementById('myform');

const handleSaveClick = (e) => {
  e.preventDefault()
  const rating = document.querySelector('input[name="rating"]:checked');

  const formData = new FormData();
  formData.append("comment_give", commentList.value);
  formData.append("rating_give", rating.value);

  console.log(formData)

  fetch("/comment", { method: "POST", body: formData })
    .then((res) => res.json())
    .then((data) => {
      alert(data["msg"]);
      window.location.reload();
    });
}


const show_order = () => {
  fetch("/comment")
    // /mars로 get요청을 보냄
    .then((res) => res.json())
    .then((data) => {
      let rows = data["result"];
      // rows라는 변수에 백엔드에서 보내준 result값을 넣어준다.
      console.log(rows)
      //       rows.forEach((row) => {
      // //가져온 result값이 담긴 rows를 반복문으로 돌린다.
      //           let name = row["name"];
      //           let address = row["address"];
      //           let size = row["size"];
      // //가져온 데이터를 변수를 만들어서 각각 넣어준다.
      //           let temp_html = `<tr>
      //                               <td>${name}</td>
      //                               <td>${address}</td>
      //                               <td>${size}</td>
      //                           </tr>`;
      //         $("#order-box").append(temp_html);
      //       });
    });
}

show_order()
commentButton.addEventListener('click', handleSaveClick);
