《Spring Cloud基础教程（Dalston版本）（强力推荐）》
https://www.cnblogs.com/edisonchou/p/java_spring_cloud_foundation_sample_list.html
2019.11.5
	1.SpringBoot简介
		spring Boot来简化Spring应用开发，约定大于配置，去繁从简，just run就能创建一个独立的，
		产品级别的应用
		1.1.1背景
			J2EE笨重的开发、繁多的配置、低下的开发效率、复杂的部署流程、第三方技术集成难度大
		1.1.2解决
			(1)Spring全家桶时代
			(2)Spring Boot->J2EE一站式解决方案
			(3)Spring Cloud->分布式整体解决方案
	2.初窥spring boot 
	
	
		2.1spring Boot 安装：
			IDEA：IntelliJ IDEA 2018.3.6.exe
			https://www.jianshu.com/p/7d60ea5e51e9
		2.2IDEA使用spring assistant插件实现spring initializer
			2.2.1File>Settings>Plugins,点击Browse repositories按钮(Spring Assistant)
                #问题：构建spring initializer时出现 failed for https://spring.io
                
                
			2.2.2 勾选Web模板
				
			2.2.3SpringBootApplication:一个带有main()方法的类，用于启动应用程序
			
			2.2.4SpringbootApplicationTests：一个空的Junit测试，它加载一个使用Spring Boot字典配置功能
				的Spring应用程序上下文
			2.2.5application.properties:一个空的properties文件，可以根据需要添加配置属性
			
			2.2.6pom.xml:Maven构建说明文件
		#编写HelloController
		2.3在包下新建一个[HelloController]
			@RestController
			public class HelloController{
				@RequestMapping("/hello")
				public String hello(){
					return "Hello Spring Boot";
				}
			}
			
		2.4利用IDEA启动Spring Boot
			在DemoApplication这个类中，运行启动：
			@SpringBootApplication
			public class DemoApplication {
				public static void main(String[] args) {
					SpringApplication.run(DemoApplication.class, args);
				}
			}
			
		2.5关于WhiteLabel Error Page(type=Not Found,status=404)
			2.5.1JSP要用到JSTL
				<%@ taglib prefix="spring" uri="http://www.springframework.org/tags" %>
				<%@ taglig prefix="c" uri="http://java.sun.com/jsp/jstl/core" %>
			2.5.2
				<dependency>
					<groupId>javax.servlet</groupId>
					<artifactId>jstl</artifactId>
				</dependency> 
				<dependency>
					<groupId>org.apache.tomcat.embed</groupId>
					<artifactId>tomcat-embed-jasper</artifactId>
					<scope>provided</scope>
				</dependency>
			
		2.6Spring Boot热部署
			在目前Spring Boot项目中，当发生了任何修改之后我们都需要重新启动才能得到正确的结果，
			spring Boot提供了热部署的方式，当发现任何类发生改变，会通过JVM类加载到虚拟机。
			2.6.1关于Spring Boot热部署失效问题
				(1)在pom.xml中添加spring-boot-devtools依赖
					<dependency>
						<groupId>org.springframework.boot</groupId>
						<artifactId>spring-boot-devtools</artifactId>
						<optional>true</optional> <!-- 这个需要为 true 热部署才有效 -->
					</dependency>
				(2)在pom文件在添加配置
					<build>
					   <plugins>
						  <plugin>
							 <groupId>org.springframework.boot</groupId>
							 <artifactId>spring-boot-maven-plugin</artifactId>
							 <configuration>            
								<fork>true</fork>
								<addResources>true</addResources>
							 </configuration>
						  </plugin>
					   </plugins>
					</build>
				(3)在idea中setting->compiler- Build project automatically勾上
				(4)使用CTRL + SHIFT + A 开启idea自动make功能
					搜索Registry->compiler.automake.allow.when.app.running 勾上
			
		2.7Spring Boot支持JSP：
			Spring Boot的默认视图支持是Thymeleaf模板引擎。
			#增加对JSP文件的支持
			2.7.1修改pom.xml增加对JSP文件的支持
				(1)servlet依赖
					<dependency>
						<groupId>javax.servlet</groupId>
						<artifactId>javax.servlet-api</artifactId>
						<scope>provided</scope>
					</dependency>
					<dependency>
						<groupId>javax.servlet</groupId>
						<artifactId>jstl</artifactId>
					</dependency>
				(2)tomcat的支持：
					<dependency>
						<groupId>org.apache.tomcat.embed</groupId>
						<artifactId>tomcat-embed-jasper</artifactId>
						<scope>provided</scope>
					</dependency>
			2.7.2关于使用idea解决新建jsp文件而找不到jsp文件模版的新建选项
				https://www.cnblogs.com/sxdcgaq8080/p/7676294.html
				(1)左上角，file中点击project Structure项，在Modules选项卡中，找到本项目，
				(2)修改Web Resource Directories：
					指定目录为:webapp
		
	3.spring Boot 的配置文件：
		#spring Boot使用一个全局的配置文件application.properties或application.yml，
		#放置在src/main/resource目录或者类路径的/config下
		'''spring Boot不仅支持常规的properties配置文件，还支持yaml语言的配置文件'''
		'''yaml是以数据为中心的语言，在配置数据的时候具有面向对象的特征'''
		3.1新建一个apllication.yml的文件
			#注意：yml需要在:后加一个空格
			server:                    @RestController
				port： 8080             public class HelloController{
			name: Remous                    @Value("${name}")    
			age: 25                         private String name; 
											@Value("${age}")
											private	Integer age;
											@RequestMapping("/hello")
											public String hello(){
												return name+age;
											}
		3.2封装配置信息：
			#这样写配置文件繁琐而且可能会造成类的臃肿，因为有许许多多的@Value注解
			@Component      //Component:表明当前类是一个Java Bean
			@ConfigurationProperties(prefix="student")        //表明获取前缀为student的配置信息
			public class StudentProperties{
				private String name;                                  server:
				private Integer age;                                     port: 8080  
				public String getName(){return name;}                 student: 
				public void setName(String name){this.name=name;}        name: Remous    
				public void getAge{return age;}                          age: 23
				public void setAge(Integer age){this.age=age;}
			}
		    #在控制器使用
			@Autowired
			private StudentProperties sduentProperties;
			@RequestMapping("/hello")
			public String hello(){return stduentProperties.getName()+studentProperties.getAge;}
		
2019/11/7
	1.集成MyBatis
		1.1第一步：修改pom.xml增加对MySQL和MyBatis的支持
		<!-- mybatis -->
			<dependency>
				<groupId>org.mybatis.spring.boot</groupId>
				<artifactId>mybatis-spring-boot-starter</artifactId>
				<version>1.1.1</version>
			</dependency>
			<!-- mysql -->
			<dependency>
				<groupId>mysql</groupId>
				<artifactId>mysql-connector-java</artifactId>
				<version>8.0.15</version>
			</dependency>
		
		1.2
		
		
	问题：
		(1)'''关于IntelliJ Idea 解决 Could not autowire. No beans of ‘xxxx' type found 的错误提示'''
			#解决方案
 			但程序的编译和运行都是没有问题的，这个错误提示并不会产生影响。
			在注解上加上：@Autowired(required = false)
		(2)'''关于Spring Boot访问不到controller'''
			#首先，出现这个异常说明了跳转页面的url无对应的值. 
			#解决方案
			确认是否扫描到了controller，Application启动类的位置是否正确
			Application启动类的位置不对，要讲Application类放置最外侧。即包含所有子包
			原因：spring-boot会自动加载启动类所在包下以及其子包下的所有组件
	
单体应用架构：
	用户管理-商品管理-订单管理
	优点：开发简单，适用于小型应用
	缺点：不易扩展，代码耦合
	
垂直应用架构：
	用户中心-商品系统-后台系统
	
	优点：解决高并发问题，针对不同模块优化，方便水平扩展，容错
	缺点：系统间相互独立，重复开发工作
	     
分布式架构：	
	展示层功能：电商系统-CMS系统-后台管理系统
			ESB总线/dubbo框架
	服务层：用户服务-订单服务-其他服务
	数据层：电商系统数据库-CMS系统数据库-后台管理系统数据库
	
	优点：抽取公共的功能为服务，提高开发效率，对不同服务进行集群化部署解决系统压力，减少系统耦合
	缺点：随着服务越来越多，服务的评估，治理，调度会出现问题（SOA,Service-Oriented Architecture）。
		抽取服务的粒度打，服务提供方与调用方接口耦合度较高
	
		
2019/11/11
	1.微服务
		2014,Martin fowler
		1.1微服务：架构风格(服务微化)
			一个应用应该是一组小型服务；可以通过HTTP的方式进行互通。
		1.2每一个功能元素最终都是一个可独立替换和独立升级的软件
		
		1.3微服务的特点：
			1.3.1单一职责：微服务中每一个服务都对应唯一的业务能力，做到单一职责，
			1.3.2微：微服务的服务拆分粒度很小，虽小单五脏俱全
			1.3.3面向服务：面向服务是说每个服务都要对外暴露服务接口API。并不关心服务的技术实现，
				 只需要提供Rest接口即可。
			1.3.4自治：自治是说服务间相互独立，互不干扰。
				(1)团队独立
				(2)技术独立
				(3)前后端分离
				(4)数据库分离
				(5)部署独立：每个服务都是独立的组件，可复用，替换、降低耦合、易维护Docker部署服务
	
	2.远程调用方式：	
		#SOA：Service-Oriented Architecture 面向服务的架构
		'''无论是微服务还是分布式服务(都是SOA，面向服务编程)，都面临着服务间的远程调用。'''
		2.1RPC：Remote Produce Call远程过程调用，类似的有RMI(Remote Method Invoke) 远程方法调用
			(1)RPC的框架：webservice(cxf)、dubbo
			(2)RMI的框架：hessian
		2.2Http：基于TCP，现在热门的Rest风格，就可以通过Http协议来实现。
		2.3总结：对比RPC和http的区别：
			2.3.1RPC并没有规定数据的传输格式，可以自己任意指定
			2.3.2Http中定义了资源传输格式，RPC中并不需要
			2.3.3RPC需要满足像调用本地服务一样调用远程服务，也就是对调用过程在API底层进行封装。
				Http协议没有这样的要求，因此请求、响应等细节需要我们自己去实现。
			2.3.4RPC要比http更快，http协议信息往往比较臃肿。
			2.3.5RPC实现较为复杂，http相对比较简单。
			2.3.6http比RPC灵活一些。
			#优点：
			(1)RPC方式更加透明，对用户更方便。
			(2)Http方式更灵活，没有规定API和语言，跨语言、平台
			缺点：
			(1)RPC方式需要在API层面进行封装，限制了开发语言环境
2019/11/12
	1.初识Spring Boot Actuator
		'''Spring Boot Actuator可以帮助你监控和管理Spring Boot应用，比如健康检查、审计、'''
		'''统计和HTTP追踪。所有这些特性可以通过JMX或者HTTP endpoints来获得。'''
		博客：https://www.jianshu.com/p/d5943e303a1f
		Actuator同时可以与外部应用监控系统整合，比如Prometheus、Graphite。
		1.1引入Spring Boot应用。
			<dependencies>
				<dependency>
					<groupId>org.springframework.boot</groupId>
					<artifactId>spring-boot-starter-actuator</artifactId>
				</dependency>
			</dependencies>
		1.2使用Actuator Endpoints来监控应用
			Actuator创建了所谓的endpoint来暴露HTTP或者JMX来监控和管理应用
			
		1.3应用默认使用8080端口运行，通过http://localhost:8080/actuator	来展示所有通过HTTP暴露的endpoints
			
		1.4打开http://localhost:8080/actuator/health	
			#如果出现{"status":"UP"} 代表"up"状态是监控的。不健康会显示"DOWN"
		1.5info endpoint http://localhost:8080/actuator/info	展示了关于应用的一般信息，这些信息从编译文件比如
			(META-INF/build-info.properties)或者Git文件比如git.properties
			
		1.6常用actuator endpoints列表	
		https://docs.spring.io/spring-boot/docs/current/reference/html/production-ready-features.html#production-ready-endpoints 
			#EndPoint ID:      Description:
			auditenvents       显示应用暴露的审计事件，比如认证进入、订单失败
			info               显示应用的基本信息。
		
		1.7显示详细的健康信息
			management：
				endpoint：
					health：
						show-details: always
			#http://localhost:8080/actuator/health
			{"status":"UP",
			"components":{
				"db":{
					"status":"UP","details":{
						"database":"MySQL",
							"result":1,
								"validationQuery":"/* ping */ SELECT 1"}},"diskSpace":
			{"status":"UP","details":{"total":2000396742656,"free":198417686528,"threshold":10485760}},"ping":{"status":"UP"}}}
			
	2.创建一个自定义的健康指标
		可以通过实现HealthIndicator接口来自定义一个健康指标，或者继承AbstractHealthIndicator类
		2.1 /metrics endpoint
		
		2.2loggers endpoint 
			可以通过访问http://localhost:8080/actuator/loggers来进入。
			它展示了应用中可配置的loggers的列表和相关的日志等级。
		
		2.2使用Spring Security来保证Actuator Endpoints安全	
	
	
	3Spring Cloud Eureka：			
		服务治理：Spring Cloud Eureka是微服务架构中最为核心和基础模块，它主要实习各个微服务实例的自动化注册与发现
		3.1服务注册：
			在服务治理框架中，通常会搭建一个注册中心，每个服务单元向注册中心登记自己提供的服务。将主机与端口号、版本号、
			通信协议等一些附加信息告知注册中心，注册中心按服务名分类组织服务清单。
		
		3.2服务发现：由于在服务治理框架下运作，服务间的调用不在通过具体实例地址来实现，而是通过向服务名发起请求调用实现。
			调用方需要向服务注册中心咨询服务，并获取所有服务的实例清单。
		3.3Netfix Eureka 
			3.3.1Eureka服务端：称为服务注册中心
			3.3.2Eureka客户端：主要处理服务的注册与发现
		3.4搭建服务注册中心
			3.4.1创建Spring Boot工程，在pom.xml引入依赖：
					<dependency>
						<groupId>org.springframework.cloud</groupId>
						<artifactId>spring-cloud-starter-eureka-server</artifactId>
					</dependency>
					
					<dependencyManagement>
						<dependencies>
							<dependency>
							   <groupId>org.springframework.cloud</groupId>
							   <artifactId>spring-cloud-dependencies</artifactId>
							   <version>Dalston.SR1</version>
							   <type>pom</type>
							   <scope>import</scope>
							</dependency>
						</dependencies>
					</dependencyManagement>
					
		3.5@EnableEurekaServer注解启动一个服务支持中心提供给其它应用	进行对话。
		
2019/11/13
	
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
