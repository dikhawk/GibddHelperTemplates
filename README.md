# GibddHelperTemplates
Шаблоны обращений в ГИБДД для андроид приложения GibddHelper https://play.google.com/store/apps/details?id=com.dik.gibddhelper
Если у вас есть конструктивные предложение по изменению шаблона обращения, либо у вас есть рецепт эффективного обращения, также вы можете создать новый, пишите в https://t.me/gibdd_helper

%date_time% - дата и время события<br/>
%address% - место происшествия<br/>
%coordinates% - кооридинаты происшествия<br/>
%yandex_map_link% - ссылка яндекс карты на место происшествие<br/>
%description% - описание события<br/>
%email% - почтовый адрес на который будет отправлен ответ<br/>

Формат шаблонов

```<template>
    <id></id>
    <name></name>
    <description></description>
    <law_links>
        <law_link>
            <title></title>
            <link></link>
        </law_link>
        <law_link>
            <title></title>
            <link></link>
        </law_link>
    </law_links>
    <fields>
        <field>
            <name></name>
            <hint></hint>
            <value></value>
            <required_field></required_field>
            <visibility></visibility>
        </field>
        <field>
            <name></name>
            <hint></hint>
            <value></value>
            <required_field></required_field>
            <visibility></visibility>
        </field>
    </fields>
    <text>
    </text>
</template>```
