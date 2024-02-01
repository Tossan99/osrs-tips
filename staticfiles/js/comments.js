
// Gets all the elements for the functions
const editButtons = document.getElementsByClassName("btn-edit");
const commentText = document.getElementById("content");
const commentForm = document.getElementById("commentForm");
const submitButton = document.getElementById("submitButton");
const commentHeading = document.getElementById("commentHeading");
const deleteModal = new bootstrap.Modal(document.getElementById("deleteModal"));
const commentDeleteButtons = document.getElementsByClassName("btn-delete-comment");
const postDeleteButtons = document.getElementsByClassName("btn-delete-post");
const deleteConfirm = document.getElementById("deleteConfirm");
const deleteModalText = document.getElementById("deleteModalText");
const deleteModalLabel = document.getElementById("deleteModalLabel");

for (let button of editButtons) {
    // Edits the targeted comment
    button.addEventListener("click", (e) => {
        let commentId = e.target.getAttribute("comment_id");
        let commentContent = document.getElementById(`comment${commentId}`).innerText;
        commentText.value = commentContent;
        submitButton.innerText = "Update";
        commentHeading.innerText = "Edit your comment";
        commentForm.setAttribute("action", `edit_comment/${commentId}`);
    });
}

for (let button of commentDeleteButtons) {
    // Triggers a modal to delete the targeted comment
    button.addEventListener("click", (e) => {
        let commentId = e.target.getAttribute("comment_id");
        deleteModalLabel.innerText = "Delete Comment?"
        deleteModalText.innerText = "Are you sure you want to delete this comment? This action cannot be undone!"
        deleteConfirm.href = `delete_comment/${commentId}`;
        deleteModal.show();
    });
}

for (let button of postDeleteButtons) {
    // Triggers a modal to delete the targeted post
    button.addEventListener("click", (e) => {
        let postId = e.target.getAttribute("post_id");
        console.log(postId)
        console.log("postId")
        deleteModalLabel.innerText = "Delete Post?"
        deleteModalText.innerText = "Are you sure you want to delete this post? This action cannot be undone!"
        deleteConfirm.href = `/post_delete/${postId}`;
        deleteModal.show();
    });
}
