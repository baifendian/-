package com.bfd.hackthon.controller;

import java.io.File;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

import org.apache.commons.io.FileUtils;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;
import org.springframework.web.servlet.ModelAndView;

import com.alibaba.fastjson.JSON;

@Controller
@RequestMapping(value="news.do")
public class IndexController extends RootController {
	
	@RequestMapping(params="method=getindexdata", method=RequestMethod.GET)
	public ModelAndView getIndexData(HttpServletRequest request, HttpServletResponse response) throws Exception {
		Map<String, Object> model = new HashMap<String, Object>();
		String path = IndexController.class.getClassLoader().getResource("").getPath();
		path = path.substring(1, path.length()-16);
		path += "data/";
//		String professionalNewsStr = FileUtils.readFileToString(new File(path + "professionalNews.data"), "utf-8");
//		String funnyNewsStr = FileUtils.readFileToString(new File(path + "funnyNews.data"), "utf-8");
//		String importNewsStr = FileUtils.readFileToString(new File(path + "importNews.data"), "utf-8");
//		String managemoney = FileUtils.readFileToString(new File(path + "managemoney.data"), "utf-8");
		String weatherStr = FileUtils.readFileToString(new File(path + "weather.data"), "utf-8");
		
		Map<String, Object> weather = (Map<String, Object>) JSON.parse(weatherStr);
//		Map<String, Object> professionalNews = (Map<String, Object>) JSON.parse(professionalNewsStr);
//		Map<String, Object> funnyNews = (Map<String, Object>) JSON.parse(funnyNewsStr);
//		Map<String, Object> importNews = (Map<String, Object>) JSON.parse(importNewsStr);
		
		/*weather begin*/
		Map<String, Object> weatherinfo = ((List<Map<String, Object>>) weather.get("HeWeather data service 3.0")).get(0);
		//空气质量
		String qlty = ((Map<String, Object>)((Map<String, Object>)weatherinfo.get("aqi")).get("city")).get("qlty").toString();
		//city
		String city = ((Map<String, Object>)weatherinfo.get("basic")).get("city").toString();
		//天气信息
		Map<String, Object> info = ((List<Map<String, Object>>)weatherinfo.get("daily_forecast")).get(0);
		//天气状况
		String cond = ((Map<String, Object>)info.get("cond")).get("txt_d").toString();
		//date
		String date = info.get("date").toString();
		//最高最低气温
		Map<String, Object> tmp = (Map<String, Object>) info.get("tmp");
		String max = tmp.get("max").toString();
		String min = tmp.get("min").toString();
		//风向
		Map<String, Object> wind = (Map<String, Object>) info.get("wind");
		String dir = wind.get("dir").toString();
		String sc = wind.get("sc").toString();
		/*weather end*/
		
		StringBuffer sb = new StringBuffer();
		sb.append(city + " ");
		sb.append(date + " ");
		sb.append(cond + " ");
		sb.append(min + "~" + max + " ");
		sb.append(qlty);
		
		model.put("weather", sb.toString());
		//行业
//		model.put("professionalnews", professionalNewsStr);
		//趣闻
//		model.put("funnynews", funnyNewsStr);
		//要闻
//		model.put("importnews", importNewsStr);
		//体育
//		model.put("sportNews", "");
		
		//理财
//		model.put("managemoney", managemoney);
		
		return makeJSONView(response, model);
	}
}
