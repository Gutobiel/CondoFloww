document.addEventListener('DOMContentLoaded', () => {
    const noticeList = document.getElementById('notice-list');
    const addNoticeBtn = document.getElementById('add-notice-btn');
    const noticeModal = document.getElementById('notice-modal');
    const noticeInput = document.getElementById('notice-input');
    const noticeText = document.getElementById('notice-text');
    const saveNoticeBtn = document.getElementById('save-notice-btn');
    const closeBtn = document.querySelector('.close');

    let notices = [];

    // Abre o modal ao clicar no botão "Adicionar Aviso"
    addNoticeBtn.addEventListener('click', () => {
        noticeInput.value = '';
        noticeText.value = '';
        noticeModal.style.display = 'block'; // Mostra o modal
    });

    // Fecha o modal ao clicar no botão de fechar
    closeBtn.addEventListener('click', () => {
        noticeModal.style.display = 'none'; // Esconde o modal
    });

    // Salva o aviso e atualiza a lista
    saveNoticeBtn.addEventListener('click', () => {
        const newNoticeTitle = noticeInput.value;
        const newNoticeText = noticeText.value;
        if (newNoticeTitle.trim() !== '' && newNoticeText.trim() !== '') {
            notices.push({ title: newNoticeTitle, text: newNoticeText });
            updateNoticeList();
            noticeModal.style.display = 'none'; // Esconde o modal após salvar
        }
    });

    // Atualiza a lista de avisos exibidos
    function updateNoticeList() {
        noticeList.innerHTML = '';
        notices.forEach((notice, index) => {
            const noticeItem = document.createElement('li');
            noticeItem.textContent = notice.title + ': ' + notice.text;
            noticeList.appendChild(noticeItem);
        });
    }

    // Chama a função para inicializar a lista
    updateNoticeList();
});
