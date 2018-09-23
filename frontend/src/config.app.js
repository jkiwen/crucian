

module.exports = {
    APP_NAME: ['documents', 'workbench'], // 应用名，按顺序对应APP_LIST元素位
    APP_LIST: [
        {
            BASE_URL: '', // 二级目录
            INDEX_HTML: 'documents', // 默认页（自动改名为index.html）
            CONTEXT_DIRECTORY: [ // 目录树结构（上接BASE_URL或DOMAIN）
                
            ]
        },
        {
            BASE_URL: '', // 二级目录
            INDEX_HTML: 'workbench', // 默认页（自动改名为index.html）
            CONTEXT_DIRECTORY: [ // 目录树结构（上接BASE_URL或DOMAIN）
                
            ]
        }
    ]
}