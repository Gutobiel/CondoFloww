const noticeList = document.getElementById('notice-list');
const addNoticeBtn = document.getElementById('add-notice-btn');
const noticeModal = document.getElementById('notice-modal');
const noticeInput = document.getElementById('notice-input');
const saveNoticeBtn = document.getElementById('save-notice-btn');
const closeBtn = document.querySelector('.close');

let notices = [];

addNoticeBtn.addEventListener('click', () => {
    noticeInput.value = '';
    noticeModal.style.display = 'block';
});

closeBtn.addEventListener('click', () => {
    noticeModal.style.display = 'none';
});

saveNoticeBtn.addEventListener('click', () => {
    const newNotice = noticeInput.value;
    if (newNotice.trim() !== '') {
        notices.push(newNotice);
        updateNoticeList();
        noticeModal.style.display = 'none';
    }
});

function updateNoticeList() {
    noticeList.innerHTML = '';
    for (let i = 0; i < notices.length; i++) {
        const noticeItem = document.createElement('li');
        noticeItem.textContent = notices[i];
        const editBtn = document.createElement('button');
        editBtn.textContent = 'Editar';
        editBtn.addEventListener('click', () => editNotice(i));
        const deleteBtn = document.createElement('button');
        deleteBtn.textContent = 'Excluir';
        deleteBtn.addEventListener('click', () => deleteNotice(i));
        noticeItem.appendChild(editBtn);
        noticeItem.appendChild(deleteBtn);
        noticeList.appendChild(noticeItem);
    }
}

function editNotice(index) {
    const editedNotice = prompt('Editar aviso:', notices[index]);
    if (editedNotice !== null) {
        notices[index] = editedNotice;
        updateNoticeList();
    }
}

function deleteNotice(index) {
    notices.splice(index, 1);
    updateNoticeList();
}

updateNoticeList();
