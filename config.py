db_info = {
    'host': '',  # 本地地址
    'user': '',  # 用户名
    'passwd': '',  # 库登录密码
    'db': '',  # 数据库名称
    'port': 3306,  # 端口号
    'charset': 'utf8'  # 编码
}

API_SERVER = ''
API_KEY = ''
UPLOADER = ''

url_list = {
    '吉林省': {
        '长春市': [
            # 'http://wjw.changchun.gov.cn/xwzx/tzgg/',  # 长春
            # 'http://wjw.changchun.gov.cn/xwzx/tzgg/index_1.html',  # 长春
        ],
        '吉林市': [
            # 'http://wjw.jlcity.gov.cn/gsgg/index.html',  # 吉林市
            # 'http://wjw.jlcity.gov.cn/gsgg/index_1.html',  # 吉林市
        ],
        '四平市': [
            # 'http://wjw.siping.gov.cn/zwgk/tzgg/',
            # 'http://wjw.siping.gov.cn/zwgk/tzgg/index_1.html'
        ],
        '辽源市': [
            # 'http://wjw.liaoyuan.gov.cn/wzsy/ggl/',
        ],
        # '通化市': ['http://www.tonghua.gov.cn/wjw/gsgk/'],
        # '松原市': ['http://wsjkw.jlsy.gov.cn/xwzx/xqjl/'],
        # '白山市': ['http://wsjkw.cbs.gov.cn/xwzx/'],
        # '白城市': ['http://wjw.jlbc.gov.cn/zwdt/'],
    },
    '辽宁省': {
        '沈阳市': [
            # 'http://wjw.shenyang.gov.cn/xxgk/tzgg/glist.html',
            # 'http://wjw.shenyang.gov.cn/sywsj/xxgk/tzgg/glist1.html',
            # 'http://wjw.shenyang.gov.cn/sywsj/xxgk/tzgg/glist2.html',
            # 'http://wjw.shenyang.gov.cn/sywsj/xxgk/tzgg/glist3.html',
            # 'http://wjw.shenyang.gov.cn/sywsj/xxgk/tzgg/glist4.html'
        ],
        # '大连市': ['http://hcod.dl.gov.cn/web/guest/20'],  # TODO:不含日期
        # '鞍山市': ['http://wjw.anshan.gov.cn/News_list.aspx?Sort_Id=34&Menu_Id=0'],
        # '抚顺市': ['http://fswjw.fushun.gov.cn/index.php?c=category&id=35'],
        # '本溪市': ['http://wjw.benxi.gov.cn/xwzx/wsjskx'],
        # '丹东市': ['http://wsjsw.dandong.gov.cn/wjw/yqfk/'],
        # '锦州市': ['http://wjw.jz.gov.cn/jzwswindex/tzgglist?id=1316'],
        # '营口市': ['http://wjw.yingkou.gov.cn/003/about.html', 'http://wjw.yingkou.gov.cn/003/2.html'],
        # '阜新市': ['http://wsjk.fuxin.gov.cn/fxswsj/gzdt/list.html'],
        # '辽阳市': ['http://wjw.liaoyang.gov.cn/lywjw/zwdt/tzgg/glist.html'],
        # '铁岭市': ['http://wjw.tieling.gov.cn/tielingws/tzgg/index.html'],
        # '盘锦市': ['http://wjw.panjin.gov.cn/col/col1757/index.html'],
        # '朝阳市': ['http://wjw.zgcy.gov.cn/Cywjj/xwzx/001001/'],
        # '葫芦岛市': ['http://wsjk.hld.gov.cn/zwgk/tzgg/'],
    },
    '黑龙江省': {
        '': ['http://wsjkw.hlj.gov.cn/index.php/Home/Zwgk/all/typeid/42'],
    },
    '天津市': {
        '': ['http://wsjk.tj.gov.cn/col/col87/index.html']
    }

}