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

MAX_NUM_FOR_ONE_SITE = 20

url_list = {
    '吉林省': {
        '长春市': [
            'http://wjw.changchun.gov.cn/xwzx/tzgg/',
            'http://wjw.changchun.gov.cn/xwzx/tzgg/index_1.html',
        ],
        '吉林市': [
            'http://wjw.jlcity.gov.cn/gsgg/index.html',
            'http://wjw.jlcity.gov.cn/gsgg/index_1.html',
        ],
        '四平市': [
            'http://wjw.siping.gov.cn/zwgk/tzgg/',
            'http://wjw.siping.gov.cn/zwgk/tzgg/index_1.html'
        ],
        '辽源市': [
            'http://wjw.liaoyuan.gov.cn/wzsy/ggl/',
        ],
        '通化市': ['http://www.tonghua.gov.cn/wjw/gsgk/'],
        '松原市': ['http://wsjkw.jlsy.gov.cn/xwzx/xqjl/'],
        '白山市': ['http://wsjkw.cbs.gov.cn/xwzx/'],
        '白城市': ['http://wjw.jlbc.gov.cn/zwdt/'],
    },
    '辽宁省': {
        '沈阳市': [
            'http://wjw.shenyang.gov.cn/xxgk/tzgg/glist.html',
            'http://wjw.shenyang.gov.cn/sywsj/xxgk/tzgg/glist1.html',
            'http://wjw.shenyang.gov.cn/sywsj/xxgk/tzgg/glist2.html',
            'http://wjw.shenyang.gov.cn/sywsj/xxgk/tzgg/glist3.html',
            'http://wjw.shenyang.gov.cn/sywsj/xxgk/tzgg/glist4.html'
        ],
        '大连市': ['http://hcod.dl.gov.cn/web/guest/20'],  # TODO:不含日期
        '鞍山市': ['http://wjw.anshan.gov.cn/News_list.aspx?Sort_Id=34&Menu_Id=0'],
        '抚顺市': ['http://fswjw.fushun.gov.cn/index.php?c=category&id=35'],
        '本溪市': ['http://wjw.benxi.gov.cn/xwzx/wsjskx'],
        '丹东市': ['http://wsjsw.dandong.gov.cn/wjw/yqfk/'],
        '锦州市': ['http://wjw.jz.gov.cn/jzwswindex/tzgglist?id=1316'],
        '营口市': ['http://wjw.yingkou.gov.cn/003/about.html', 'http://wjw.yingkou.gov.cn/003/2.html'],
        '阜新市': ['http://wsjk.fuxin.gov.cn/fxswsj/gzdt/list.html'],
        '辽阳市': ['http://wjw.liaoyang.gov.cn/lywjw/zwdt/tzgg/glist.html'],
        '铁岭市': ['http://wjw.tieling.gov.cn/tielingws/tzgg/index.html'],
        '盘锦市': ['http://wjw.panjin.gov.cn/col/col1757/index.html'],
        '朝阳市': ['http://wjw.zgcy.gov.cn/Cywjj/xwzx/001001/'],
        '葫芦岛市': ['http://wsjk.hld.gov.cn/zwgk/tzgg/'],
    },
    '黑龙江省': {
        '省': ['http://wsjkw.hlj.gov.cn/index.php/Home/Zwgk/all/typeid/42'],
    },
    '天津市': {
        '省': ['http://wsjk.tj.gov.cn/col/col87/index.html']
    },
    '内蒙古自治区': {
        '省': ['http://wjw.nmg.gov.cn/xwzx/xwfb/index.shtml'],
        '赤峰市': ['https://wjw.chifeng.gov.cn/index.php?g=Home&m=List&a=index&lmid=56'],
        '呼和浩特市': ['http://wjw.huhhot.gov.cn/zwdt/gzdt/'],
        '包头市': ['http://wjw.baotou.gov.cn/wsyw/'],
        '乌海市': ['http://wjw.wuhai.gov.cn/wsj/xxgk/xwfb/index.html'],
        '通辽市': ['http://wjw.tongliao.gov.cn/wjw/sjyw/list.shtml'],
        '鄂尔多斯市': ['http://wjw.ordos.gov.cn/zxdt/index.html'],
        '呼伦贝尔市': ['http://wjw.hlbe.gov.cn/szdt/'],
        '巴彦卓尔市': ['http://wjw.bynr.gov.cn/html/zwgk/tzgg/index.html'],
        '乌兰察布市': ['http://wjw.wulanchabu.gov.cn/channel/wlcb_wjw/col22734f.html'],
    },
    '安徽省': {
        '合肥市': ['http://wjw.hefei.gov.cn/xwzx/tzgg/index.html'],    # TODO: 需js先写入cookie
        '安庆市': ['http://wjw.anqing.gov.cn/13971952.html'],
        '蚌埠市': ['http://wjw.bengbu.gov.cn/gzdt/'],
        '亳州市': ['http://wjw.bozhou.gov.cn/News/showList/5275/page_1.html'],
    },
    '四川省': {
        '省': ['http://wsjkw.sc.gov.cn/scwsjkw/gzbd01/ztwzlmgl.shtml'],
        '成都市': ['http://cdwjw.chengdu.gov.cn/cdwjw/c135634/list.shtml'],    # TODO: get 0
        '眉山市': ['http://swjw.ms.gov.cn/tzgg.htm'],
        '宜宾市': ['http://ybwjw.yibin.gov.cn/gzdt/'],
        '德阳市': ['https://wjw.deyang.gov.cn/gggs/'],
        '南充市': ['http://wsjsw.nanchong.gov.cn/html/2020xghyfk/'],   # TODO: get 0，有WAF检查浏览器
        '乐山市': ['http://swjj.leshan.gov.cn/swjj/yqtb/list.shtml'],
        '绵阳市': ['http://wjw.my.gov.cn/ggl/index.html'],
        '自贡市': ['http://www.zg.gov.cn/web/swsjsw/dep_gzdt'],
        '雅安市': ['http://wjw.yaan.gov.cn/xinwen/list/d3869429-e6f6-4d6d-a9a0-bcfc1ed7b08b.html'],
        '泸州市': ['http://wjw.luzhou.gov.cn/xwdt/gzdt'],
        '内江市': ['http://wsj.neijiang.gov.cn/list/%E5%B7%A5%E4%BD%9C%E5%8A%A8%E6%80%81'],
        '达州市': ['http://wjw.dazhou.gov.cn/Html/zhengwugongkai/gongshigonggao/'],
    },
    '宁夏回族自治区': {
        '省': ['http://wsjkw.nx.gov.cn/yqfkdt/yqsd1.htm'],
        '银川': ['http://wjw.yinchuan.gov.cn/wsjsdt/index.htm'],
    },
    '青海省': {
        '省': ['https://wsjkw.qinghai.gov.cn/ztbd/yqjk/yqtb/index.html'],
    },
    '甘肃省': {
        '省': ['http://wsjk.gansu.gov.cn/channel/list/11218.html'],
        '兰州': ['http://wjw.lanzhou.gov.cn/col/col14897/index.html'],    # TODO: get 0 云防护
        '酒泉': ['http://wjw.jiuquan.gov.cn/xinwenzhongxin/weijianxinwen/'],
        '嘉峪关': ['http://wjw.jyg.gov.cn/tzgg/'],
        '白银': ['http://wjw.baiyin.gov.cn/html/gzdt/tongzhigonggao/index.shtml'],
        '金昌': ['http://wjw.jcs.gov.cn/col/col20369/index.html'],
        '张掖': ['http://www.zhangye.gov.cn/wjw/dzdt/gzdt/'],
        '平凉': ['http://wjw.pingliang.gov.cn/tzgg/'],
        '甘南藏族自治州': ['http://wsjk.gnzrmzf.gov.cn/gzdt.htm'],
    },
    '陕西省': {
        '省': ['http://sxwjw.shaanxi.gov.cn/col/col9/index.html?uid=572&pageNum=1'],
    },
}

rest_urls = [
    ('河北', '唐山', 'http://wsjkwyh.tangshan.gov.cn/tswjw/tswjw_wjdt/'),
    ('河北', '秦皇岛', 'http://wjw.qhd.gov.cn/home/list?code=8&pcode=1'),
    ('河北', '邯郸', 'http://wjw.hd.gov.cn/news/10_15_1.shtml'),
    ('河北', '邢台', 'http://wsjkw.xingtai.gov.cn/Item/list.asp?id=1747'),
    ('河北', '保定', 'http://www.bdswjw.gov.cn/textlist.jsp?urltype=tree.TreeTempUrl&wbtreeid=1017'),
    ('河北', '廊坊', 'http://wjw.lf.gov.cn/tzggfkzl/index.jhtml#'),
    ('河北', '衡水', 'http://wjw.hengshui.gov.cn/col/col2548/index.html'),
    ('山西', '大同', 'http://www.dt.gov.cn/dtxxgk/xxgktree/list.jsp?parentChannelId=302f1736b57c49d0bb6334d24165972b'),
    ('山西', '朔州', 'http://www.shuozhou.gov.cn/xwzx/jrsz/szsyw/'),
    ('山西', '晋中', 'http://wjw.sxjz.gov.cn/gzdt/wjyw'),
    ('辽宁', '沈阳', 'http://wjw.shenyang.gov.cn/xwzx/jrtt/glist.html'),
    ('辽宁', '锦州', 'http://wjw.jz.gov.cn/jzwswindex/gzdtlist?id=1356'),
    ('辽宁', '铁岭', 'http://wjw.tieling.gov.cn/tielingws/zwgk83/index.html'),
    ('黑龙江', '哈尔滨', 'http://www.harbin.gov.cn/col/col98/index.html'),
    ('江苏', '南京', 'http://wjw.nanjing.gov.cn/njswshjhsywyh/214/index_9492.html?chnlid=35134'),
    ('江苏', '徐州', 'http://ws.xz.gov.cn/wsj/xzswshjhsywyh/028004/'),
    ('江苏', '常州', 'http://wjw.changzhou.gov.cn/class/IMNPOFCI'),
    ('江苏', '苏州', 'http://wsjkw.suzhou.gov.cn/szswjw/gsgg/list.shtml'),
    ('江苏', '南通', 'http://wjw.nantong.gov.cn/ntswjw/gggs/gggs.html'),
    ('江苏', '连云港', 'http://wjw.lyg.gov.cn/lygswjw/gzdt/gzdt.html#'),
    ('江苏', '淮安', 'http://wjw.huaian.gov.cn/wjyw/wjyw/list.html'),
    ('江苏', '盐城', 'http://wsj.yancheng.gov.cn/col/col2424/index.html'),
    ('江苏', '扬州', 'http://wjw.yangzhou.gov.cn/yzwshjh/tzgg/wjw_list.shtml'),
    ('江苏', '镇江', 'http://wjw.zhenjiang.gov.cn/xwzx/mtyq/'),
    ('江苏', '泰州', 'http://wjw.taizhou.gov.cn/col/col25806/index.html'),
    ('江苏', '宿迁', 'http://wsj.suqian.gov.cn/swsj/wsyw/list_wz.shtml'),
    ('安徽', '芜湖', 'http://wsjkw.wuhu.gov.cn/xwdt/tzgg/index.html'),
    ('安徽', '淮南', 'http://wjw.huainan.gov.cn/xwzx/tzgg/index.html'),
    ('安徽', '淮北', 'http://wjw.huaibei.gov.cn/xxfb/tzgg/index.html'),
    ('安徽', '铜陵', 'http://wsjkw.tl.gov.cn/1982/1983/'),
    ('安徽', '黄山', 'http://wjw.huangshan.gov.cn/BranchOpennessContent/showList/10395/0/page_1.html'),
    ('安徽', '滁州', 'http://wjw.chuzhou.gov.cn/5341652.html'),
    ('安徽', '阜阳', 'http://wjw.fy.gov.cn/content/channel/5c35be0048787ad14d009190/'),
    ('安徽', '宿州', 'http://wjw.ahsz.gov.cn/27543920.html'),
    ('安徽', '六安', 'http://wjw.luan.gov.cn/zwzx/gsgg/index.html'),
    ('安徽', '池州', 'http://wjw.chizhou.gov.cn/News/showList/2718/page_1.html'),
    ('安徽', '宣城', 'http://wjw.xuancheng.gov.cn/News/showList/3358/page_1.html'),
    ('福建', '三明', 'http://wjw.sm.gov.cn/xxgk/wjyw/sjdt/'),
    ('福建', '漳州', 'http://wjw.zhangzhou.gov.cn/cms/html/zzswshjhsywyh/yqfkdt/index.html'),
    ('福建', '宁德', 'http://wjw.ningde.gov.cn/xwdt/gzdt/'),
    ('江西', '景德镇', 'http://wsjs.jdz.gov.cn/zwfw/087002/moreinfo.html'),
    ('山东', '东营', 'http://dywsjk.dongying.gov.cn/col/col37165/index.html'),
    ('山东', '滨州', 'http://wjw.binzhou.gov.cn/xinwen/class/?0.html'),
    ('广西', '南宁', 'http://wjw.nanning.gov.cn/gzdt/bjdt/'),
    ('广西', '柳州', 'http://wjw.liuzhou.gov.cn/xwzx/sjxw/'),
    ('广西', '桂林', 'http://wjw.guilin.gov.cn/gzdt/bw/'),
    ('广西', '北海', 'http://xxgk.beihai.gov.cn/bhswshjhsywyh/tzgg_84785/'),
    ('广西', '钦州', 'http://zwgk.qinzhou.gov.cn/auto2540/gzdt_3159/'),
    ('广西', '玉林', 'http://wjw.yulin.gov.cn/yulinshiweishenghejhsywyh/zwyw'),
    ('广西', '河池', 'http://wjw.hechi.gov.cn/gggs/index.shtml'),
    ('广西', '来宾', 'http://wjw.laibin.gov.cn/Web/Content_Total.aspx?channel_id=319&SearchTxt='),
    ('海南', '海口', 'http://wjw.haikou.gov.cn/ywdt/zwdt/'),
    ('海南', '三亚', 'http://ws.sanya.gov.cn/wjwsite/gzdt/list2.shtml'),
    ('四川', '攀枝花', 'http://wjw.panzhihua.gov.cn/zwgk/tzgg/index.shtml'),
    ('四川', '广元', 'http://wsjsw.cngy.gov.cn/new/list/20190729172751108.html'),
    ('四川', '遂宁', 'http://swjw.suining.gov.cn/web/swjw/wsyw'),
    ('四川', '广安', 'http://wjw.guang-an.gov.cn/gaswshjhsywyh/wsxw/list.shtml'),
    ('四川', '巴中', 'http://wsjkw.cnbz.gov.cn/moreList.html?id_minor=4&id_main=1&toName='),
    ('四川', '资阳', 'http://swjw.ziyang.gov.cn/?m=content&c=index&a=lists&catid=22'),
    ('四川', '阿坝', 'http://wjw.abazhou.gov.cn/abwjw/c100004/common_list.shtml'),
    ('四川', '甘孜', 'http://wjw.gzz.gov.cn/preview/channel/818.jhtml'),
    ('四川', '凉山', 'http://wjw.lsz.gov.cn/xwzx/zwjwdt/'),
    ('陕西', '延安', 'http://wjw.yanan.gov.cn/rsf/site/yaswsj/weijiyaowen/index.html'),
    ('陕西', '汉中', 'http://wj.hanzhong.gov.cn/xwdt/sjdt/'),
    ('陕西', '安康', 'http://wjj.ankang.gov.cn/Node-6891.html'),
    ('甘肃', '兰州', 'http://wjw.lanzhou.gov.cn/col/col14897/index.html###'),
    ('甘肃', '天水', 'http://www.tianshui.gov.cn/col/col352/index.html'),
    ('宁夏', '石嘴山', 'http://wjw.shizuishan.gov.cn/xwzx/gzdt/'),
    ('贵州省', '省', 'http://www.gzhfpc.gov.cn/xwzx_500663/zwyw/'),
    ('云南省', '省',
     'http://ynswsjkw.yn.gov.cn/wjwWebsite/web/col?id=UU157976428326282067&cn=xxgzbd&pcn=ztlm&pid=UU145102906505319731'),
    ('西藏自治区', '省', 'http://wjw.xizang.gov.cn/xwzx/wsjkdt/'),
]

