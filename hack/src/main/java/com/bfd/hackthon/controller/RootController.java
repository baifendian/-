package com.bfd.hackthon.controller;

import java.io.Writer;

import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

import org.apache.commons.lang.StringUtils;
import org.apache.commons.logging.Log;
import org.apache.commons.logging.LogFactory;
import org.springframework.web.servlet.ModelAndView;

import com.alibaba.fastjson.JSON;



/**
 * 
 * @author Yuet
 * 2016年7月7日
 */
public class RootController {
	private final static Log log = LogFactory.getLog(RootController.class);

	protected ModelAndView makeJSONView(HttpServletResponse response,
			Object model) throws Exception {
		response.setCharacterEncoding("UTF-8");
		response.setContentType("application/json");
		response.setHeader("Access-Control-Allow-Origin", "*");
		log.info("return json view: " + model);
		Writer writer = response.getWriter();
		writer.write(JSON.toJSONString(model));
		writer.flush();
		writer.close();
		return null;
	}
	
	protected int getInt(HttpServletRequest request, String parameterName, int defaultValue) {
		if (StringUtils.isEmpty(parameterName)) {
			return defaultValue;
		}
		
		try {
			String value = request.getParameter(parameterName);
			return Integer.parseInt(value);
		} catch (Exception e) {
			return defaultValue;
		}
	}
	
	protected String getString(HttpServletRequest request, String parameterName) {
		if (StringUtils.isEmpty(parameterName)) {
			return null;
		}
		
		try {
			return request.getParameter(parameterName);
		} catch (Exception e) {
			return null;
		}
	}
	
	protected char[] getChars(HttpServletRequest request, String parameterName) {
		if (StringUtils.isEmpty(parameterName)) {
			return "".toCharArray();
		}
		
		try {
			return request.getParameter(parameterName).toCharArray();
		} catch (Exception e) {
			return "".toCharArray();
		}
	}
}
